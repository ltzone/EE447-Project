import time
from celery import shared_task



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