from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import TaskSerializer
from django_celery_results.models import TaskResult
# Create your views here.
from . import tasks
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def submit_task(request):
    """
    获取，更新或删除一个snippet实例。
    """
    code = request.data["code"]
    res=tasks.general_exec.delay(code)  
    #任务逻辑  
    return Response({'status':'successful','task_id':res.task_id})

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


def task_list(request):
    if request.method == 'GET':
        res = TaskResult.objects.all()
        serializer = TaskSerializer(res, many=True)
        return JSONResponse(serializer.data)
