from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import TaskSerializer, TaskResSerializer
from django_celery_results.models import TaskResult
# Create your views here.
from . import tasks
from django_celery_monitor.models import TaskState

def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

def ctest(request,*args,**kwargs):  
    res=tasks.hello.delay()  
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


def task_result_list(request):
    if request.method == 'GET':
        res = TaskResult.objects.all()
        serializer = TaskResSerializer(res, many=True)
        return JSONResponse(serializer.data)

def task_list(request):
    if request.method == 'GET':
        res = TaskState.objects.all()
        serializer = TaskSerializer(res, many=True)
        return JSONResponse(serializer.data)
