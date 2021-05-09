import os
import time
from celery import Celery

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
def mapper():
    #split your problem in embarrassingly parallel maps 
    maps = [map.s(), map.s(), map.s(), map.s(), map.s(), map.s(), map.s(), map.s()]
    #and put them in a chord that executes them in parallel and after they finish calls 'reduce'
    mapreduce = app.chord(maps)(reduce.s())    
    return "{0} mapper ran on {1}".format(app.current_task.request.id, app.current_task.request.hostname)

@app.task(name='ic.map')
def map():
    #do something useful here
    import time
    time.sleep(10.0)
    return "{0} map ran on {1}".format(app.current_task.request.id, app.current_task.request.hostname)

@app.task(name='ic.reduce')
def reduce(results):
    #put the maps together and do something with the results
    return "{0} reduce ran on {1}".format(app.current_task.request.id, app.current_task.request.hostname)