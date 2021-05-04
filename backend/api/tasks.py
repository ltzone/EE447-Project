
from celery import shared_task

@shared_task
def hello():
    raise KeyError("Error")
    # return "hello"