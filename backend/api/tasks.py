import time
from celery import shared_task

@shared_task
def general_exec(code):
    ret_val = None
    if type(code) is not str:
        return 1
    else:
        code += "\n\nret_val = main()"
    exec(code)
    return ret_val


@shared_task
def hello():
    # print("10000")
    # raise KeyError("Error")
    return "hello"

@shared_task
def sleep_task():
    time.sleep(30)
    return f"Sleeped"