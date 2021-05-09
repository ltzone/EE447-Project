from time import sleep
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get', views.task_list),
    path('test', views.ctest),
    path('sleep', views.sleep)
]