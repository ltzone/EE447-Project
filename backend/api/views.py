from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from . import tasks
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def submit_task(request, pk):
    """
    获取，更新或删除一个snippet实例。
    """
    code = request.data.code
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
