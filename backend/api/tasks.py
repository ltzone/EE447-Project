import time
from celery import shared_task
from django.db import models
from django_celery_monitor.models import TaskState
from django.utils.translation import ugettext_lazy as _
from django_celery_monitor.managers import TaskStateQuerySet

@shared_task
def general_exec(code):
    if type(code) is not str:
        return 1
    else:
        code += "\n\nret_val = main()"
    ldict = {}
    exec(code,globals(),ldict)
    return ldict.get("ret_val")

@shared_task
def hello():
    return "hello"

@shared_task
def sleep_task():
    time.sleep(30)
    return f"Sleeped"

class TaskwithCustomTaskName(TaskState):

    custom_taskname = models.CharField(_('custom task name'), max_length=200, null=True, db_index=True,)