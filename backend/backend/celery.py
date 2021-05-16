import os
import time
from celery import Celery
from celery import chord
import random
import itertools

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

app = Celery('proj')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

@app.task(name='ic.mapper')
def mapper(mapper_num, input, mapper_code, reducer_code):
    input_size = len(input)
    seg_size = int(input_size/mapper_num) + 1
    mapper_input = [input[i:i+seg_size] for i in range(0, input_size, seg_size)]
    #split the problem in parallel maps 
    maps = [map.s(mapper_input[i], mapper_code) for i in range(mapper_num)]
    #and put them in a chord that executes them in parallel and after they finish calls 'reduce'
    mapreduce = chord(maps)(reduce.s(reducer_code))
    return "{0} mapper ran on {1}".format(app.current_task.request.id, app.current_task.request.hostname)

@app.task(name='ic.map')
def map(mapper_input, mapper_code):
    #do something useful here
    ldict = {"mapper_input": mapper_input}
    if type(mapper_code) is not str:
        return []
    else:
        mapper_code += "\n\nret_val = mapper(mapper_input)"
    exec(mapper_code,globals(),ldict)
    import time
    time.sleep(random.randint(0,5))
    return ldict.get("ret_val")

@app.task(name='ic.reduce')
def reduce(mapper_outputs, reducer_code):
    joined_input = list(itertools.chain.from_iterable(mapper_outputs))
    joined_input.sort()
    #put the maps together and do something with the results
    ldict = {"joined_input": joined_input}
    if type(reducer_code) is not str:
        return None
    else:
        reducer_code += "\n\nret_val = reducer(joined_input)"
    exec(reducer_code,globals(),ldict)
    return ldict.get("ret_val")