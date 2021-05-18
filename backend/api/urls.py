from time import sleep
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # 得到运行结果 TaskResult列表
    path('get', views.task_result_list),

    # 得到task运行实时状态 TaskState列表
    path('tasks', views.task_list),

    # 仅用于调试的简单任务，
    path('test', views.ctest),
    path('sleep', views.sleep),

    # 提交任务
    path('submit', views.submit_task),

    # 提交mapreduce任务
    path('mapreduce', views.submit_map_reduce),

    # 根据request.data.get("state")筛选特定state的TaskState
    path('filtertask', views.filter_task),

    # 根据request.data.get("state")筛选特定state的TaskResult
    path('filterresult', views.filter_task_result),

    # 筛选出reduce任务的TaskState，无需参数
    path('filterreduce', views.filter_reduce),

    # 根据request.data.get("custom_task_name")筛选特定自定义用户名的TaskState
    path('tasks2', views.task_list_with_customtaskname)
]