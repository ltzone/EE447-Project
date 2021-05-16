from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import TaskSerializer, TaskResSerializer, TaskwithCustomTaskNameSerializer
from django_celery_results.models import TaskResult
# Create your views here.
from . import tasks
from .tasks import TaskwithCustomTaskName
from django_celery_monitor.models import TaskState
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from backend.celery import mapper

MAX_FILE_LEN = 1000000


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
    res=tasks.general_exec.delay(code)
    return Response({'status':'successful','task_id':res.task_id})

def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

def ctest(request,*args,**kwargs):  
    res=mapper.delay(2, ["alice hello", "bob hello", "bye alice", "bye bob", "alice and bob"], "def mapper(input):\n\toutput = []\n\tfor line in input:\n\t\tline=line.strip()\n\t\twords=line.split()\n\t\tfor word in words:\n\t\t\toutput.append(f\"{word}\t1\")\n\treturn output", "def reducer(input):\n\treturn input")
    #任务逻辑  
    return JsonResponse({'status':'successful','task_id':res.task_id})

def sleep(request,*args,**kwargs):
    res=tasks.sleep_task.delay()
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
    return JSONResponse(serializer.data)

# 用法: http://127.0.0.1:8000/api/filtertask?state=SUCCESS 返回json，下同
@api_view(['GET'])
def filter_task(request:HttpRequest):
    query_state = request.GET['state'] # request.GET返回的是QueryDict类型的字典
    res = TaskState.objects.filter(state=query_state)
    serializer = TaskSerializer(res, many=True)
    return JSONResponse(serializer.data)

@api_view(['GET'])
def filter_task_result(request):
    query_state = request.GET['state']
    res = TaskResult.objects.filter(status=query_state)
    serializer = TaskResSerializer(res, many=True)
    return JSONResponse(serializer.data)

@api_view(['GET'])
def task_list_with_customtaskname(request):
    res = TaskwithCustomTaskName.objects.all()
    serializer = TaskwithCustomTaskNameSerializer(res, many=True)
    return JSONResponse(serializer.data)