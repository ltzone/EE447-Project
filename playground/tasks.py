from celery import Celery

app = Celery('tasks', backend='redis://localhost:6379', broker='pyamqp://')

@app.task
def add(x, y):
    return x + y