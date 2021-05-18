from time import sleep
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get', views.task_result_list),
    path('tasks', views.task_list),
    path('test', views.ctest),
    path('sleep', views.sleep),
    path('submit', views.submit_task),
    path('mapreduce', views.submit_map_reduce),
    path('filtertask', views.filter_task),
    path('filterresult', views.filter_task_result),
    path('filterreduce', views.filter_reduce),
    path('tasks2', views.task_list_with_customtaskname),
    path('rdd', views.submit_general_rdd)
]