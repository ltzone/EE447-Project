import time
from celery import shared_task

@shared_task
def hello():
    # print("10000")
    # raise KeyError("Error")
    return "hello"

@shared_task
def sleep_task():
    time.sleep(30)
    return f"Sleeped"