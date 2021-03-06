import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django_celery_results.models import TaskResult
# Create your views here.
from django_celery_monitor.models import TaskState
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from backend.celery import mapper, general_rdd
from .serializers import *
from . import tasks
from .models import TaskName


MAX_FILE_LEN = 1000000

@api_view(['POST'])
def submit_general_rdd(request):
    """
    提交一个RDD任务，输入格式
    @data.taskML = [
      [
        {
          type: 'mapper/reducer/sort/group',
          name: string,
          numWorker: int,
          input: int(0,1,...), (表示在files中的index)
          action: true/false, (表示是否要出现在task_result/finished_task中)
          code: string,
        }
      ]
    ]
    @data.files = list of files
    """
    taskML = json.loads(request.data["taskML"])
    files = request.data.getlist('files')
    
    file_strings = []
    for file in files:
        with file.open('r') as f:
            file_string = []
            for l in f.readlines():
                file_string.append(l.decode('UTF-8'))
            file_strings.append(file_string)
            
    
    res = general_rdd.delay([], taskML, file_strings)
    return JsonResponse({'status':'successful','task_id':res.task_id})


@api_view(['POST'])
def submit_map_reduce(request):
    """
    获取，更新或删除一个snippet实例。
    """
    mapper_code = request.data["mapper_code"]
    reducer_code = request.data["reducer_code"]
    mapper_num = int(request.data["mapper_num"])
    file = request.data["file"]
    file_content = []
    with file.open() as f:
        cnt = 0
        while cnt < MAX_FILE_LEN:
            line = f.readline().decode('UTF-8')
            if not line:
                break
            cnt += 1
            file_content.append(line)
    res=mapper.delay(mapper_num, file_content, mapper_code, reducer_code)
    return JsonResponse({'status':'successful','task_id':res.task_id})

@api_view(['POST'])
def submit_task(request):
    """
    获取，更新或删除一个snippet实例。
    """
    code = request.data["code"]
    custom_task_name = request.data.get("custom_task_name")
    if custom_task_name is None:
        custom_task_name = "default_name"
    res=tasks.general_exec.delay(code)
    new_task = TaskName(custom_task_name=custom_task_name, task_id=res.task_id)
    new_task.save()
    return Response({'status':'successful','task_id':res.task_id})

def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

def ctest(request,*args,**kwargs):  
    res=mapper.delay(2, ["alice hello", "bob hello", "bye alice", "bye bob", "alice and bob"], "def mapper(input):\n\toutput = []\n\tfor line in input:\n\t\tline=line.strip()\n\t\twords=line.split()\n\t\tfor word in words:\n\t\t\toutput.append(f\"{word}\t1\")\n\treturn output", "def reducer(input):\n\treturn input")
    #任务逻辑  
    return JsonResponse({'status':'successful','task_id':res.task_id})

def sleep(request,*args,**kwargs):
    custom_task_name = "hello"
    if custom_task_name is None:
        custom_task_name = "default_name"
    res=tasks.sleep_task.delay()
    new_task = TaskName(custom_task_name=custom_task_name, task_id=res.task_id)
    new_task.save()
    return JsonResponse({'status':'successful','task_id':res.task_id})

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@api_view(['GET'])
def task_result_list(request):
    res = TaskResult.objects.all()
    serializer = TaskResSerializer(res, many=True)
    return JSONResponse(serializer.data)

@api_view(['GET'])
def task_list(request):
    res = TaskState.objects.all()
    serializer = TaskSerializer(res, many=True)
    ans = list()
    for item in serializer.data:
        temp_dict = item.copy()

        # 加入custom_task_name字段
        if TaskName.objects.filter(task_id=item['task_id']).count() == 0:
            custom_task_name = 'none'
        else:
            task_name_obj = TaskName.objects.get(task_id=item['task_id'])
            task_name_serializer = TaskNameSerializer(task_name_obj)
            custom_task_name = task_name_serializer.data['custom_task_name']
        temp_dict['custom_task_name'] = custom_task_name

        # 把worker字段从id转为hostname
        worker_id = temp_dict['worker']
        worker_obj = WorkerState.objects.get(id=worker_id)
        worker_name = WorkerStateSerializer(worker_obj).data["hostname"]
        temp_dict['worker'] = worker_name

        ans.append(temp_dict)
    return JSONResponse(ans)

@api_view(['GET'])
def filter_task(request:HttpRequest):
    query_state = request.data.get('state')
    res = TaskState.objects.filter(state=query_state)
    serializer = TaskSerializer(res, many=True)
    return JSONResponse(serializer.data)

@api_view(['GET'])
def filter_task_result(request):
    query_state = request.data.get('state')
    res = TaskResult.objects.filter(status=query_state)
    serializer = TaskResSerializer(res, many=True)
    return JSONResponse(serializer.data)

@api_view(['GET'])
def filter_reduce(request:HttpRequest):
    res = TaskState.objects.filter(name="ic.reduce")
    serializer = TaskSerializer(res, many=True)
    return JSONResponse(serializer.data)

@api_view(['GET'])
def task_list_with_customtaskname(request:HttpRequest):
    query_custom_task_name = request.data.get("custom_task_name")
    task_name_object = TaskName.objects.filter(custom_task_name=query_custom_task_name)
    task_name_serializer = TaskNameSerializer(task_name_object, many=True)

    id2name = dict()
    for item in task_name_serializer.data:
        id2name[item["task_id"]] = item["custom_task_name"]

    ans = list()

    for idx, ctm_name in id2name.items():
        temp_dict = dict()
        res = TaskState.objects.get(task_id=idx)
        serializer = TaskSerializer(res)
        temp_dict = serializer.data.copy()
        temp_dict['custom_task_name'] = ctm_name
        ans.append(temp_dict)

    return JSONResponse(ans)

@api_view(['GET'])
def get_result_by_taskid(request):
    query_id = request.data.get('task_id')
    res = TaskResult.objects.get(task_id=query_id)
    serializer = ResultSerializer(res)
    return JSONResponse(serializer.data) # 返回一个{"result":...}的字典

@api_view(['GET'])
def list_workers(request):
    res = WorkerState.objects.all()
    serializer = WorkerStateSerializer(res, many=True)
    return JSONResponse(serializer.data) # 返回一个{"hostname":..., "last_heartbeat":..., "last_update":...}的字典