from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from . import tasks


def index(request):
    return HttpResponse("Hello, world. You're at the api index.")



def ctest(request,*args,**kwargs):  
    res=tasks.hello.delay()  
    #任务逻辑  
    return JsonResponse({'status':'successful','task_id':res.task_id})

def sleep(request,*args,**kwargs):  
    res=tasks.sleep_task.delay()
    return JsonResponse({'status':'successful','task_id':res.task_id})
