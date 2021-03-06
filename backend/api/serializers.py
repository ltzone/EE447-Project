from rest_framework import serializers
from django_celery_results.models import TaskResult
from django_celery_monitor.models import TaskState, WorkerState
from .models import TaskName


class TaskResSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskResult
        fields = ('task_id', 'task_name', 'task_args', 'task_kwargs',
                  'status', 'worker', 'content_type', 'content_encoding',
                  'date_created', 'date_done', 'traceback', 'meta')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskState
        fields = ('state', 'task_id', 'name', 'tstamp', 'args',
                  'kwargs', 'eta', 'expires', 'result', 'traceback', 'runtime',
                  'retries', 'worker', 'hidden')


class TaskNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskName
        fields = ("custom_task_name", "task_id")

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskResult
        fields = list(['result'])

class WorkerStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerState
        fields = ("hostname", "last_heartbeat", "last_update")