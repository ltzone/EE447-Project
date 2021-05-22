import json
import os
import time
from celery import Celery
from celery import chord
import random
import itertools

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

MAX_FILE_LEN = 1000000

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


"""
RDD Inteface
"""

@app.task(name='rdd.launcher')
def general_rdd(last_tasks, taskML, file_string):
    if (len(taskML) == 0):
        return "Success"

    last_output = []
    for task_res in last_tasks:
        last_output += task_res


    def launch_task(last_output, task):
        if task["type"] == 'mapper':
            file_content = file_string[task["input"]]
            # file_content = []
            # for line in file_string[task["input"]]:
            #     file_content.append(line.decode('UTF-8'))
            # file_content = []
            # with files[task["input"]].open() as f:
            #     cnt = 0
            #     while cnt < MAX_FILE_LEN:
            #         line = f.readline().decode('UTF-8')
            #         if not line:
            #             break
            #         cnt += 1
            #         file_content.append(line)
            input_size = len(file_content)
            seg_size = int(input_size/task["numWorker"]) + 1
            mapper_input = [file_content[i:i+seg_size] for i in range(0, input_size, seg_size)]
            return [rdd_map.s(mapper_input[i], task["code"]) for i in range(task["numWorker"])]
        elif task["type"] == 'reducer':
            return [rdd_reduce.s(last_output, task["code"])]
        elif task["type"] == 'sort':
            return [rdd_sort.s(last_output)]
        elif task["type"] == 'group':
            return [rdd_group.s(last_output)]

    all_tasks = []
    for task in taskML[0]:
        all_tasks += launch_task(last_output, task)
        
    next_round_launcher = chord(all_tasks)(general_rdd.s(taskML[1:], file_string))



@app.task(name='rdd.map')
def rdd_map(mapper_input, mapper_code):
    ldict = {"mapper_input": mapper_input}
    if type(mapper_code) is not str:
        return []
    else:
        mapper_code += "\n\nret_val = mapper(mapper_input)"
    exec(mapper_code,globals(),ldict)
    import time
    time.sleep(random.randint(0,5))
    return ldict.get("ret_val")

@app.task(name='rdd.reduce')
def rdd_reduce(joined_input, reducer_code):
    ldict = {"joined_input": joined_input}
    if type(reducer_code) is not str:
        return None
    else:
        reducer_code += "\n\nret_val = reducer(joined_input)"
    exec(reducer_code,globals(),ldict)
    return ldict.get("ret_val")

@app.task(name='rdd.sort')
def rdd_sort(last_output):
    last_output.sort()
    return last_output

@app.task(name='rdd.group')
def rdd_group(last_output):
    output_dict = {}
    for line in last_output:
        line_split = line.split('\t', 1)
        key = line_split[0]
        value = line_split[1] if len(line_split) > 1 else ""
        if key not in output_dict.keys():
            output_dict[key] = set()
        output_dict[key].add(value)
    output_list = []
    for k,vs in output_dict.items():
        for v in vs:
            output_list.append(k +'\t' + v)
    return output_list

"""
Map Reduce Inteface
"""

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