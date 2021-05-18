from rest_framework import serializers
from django_celery_results.models import TaskResult
from django_celery_monitor.models import TaskState
from .tasks import TaskwithCustomTaskName


class TaskResSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskResult
        fields = ('task_id', 'task_name', 'task_args', 'task_kwargs',
                  'status', 'worker', 'content_type', 'content_encoding',
                  'result', 'date_created', 'date_done', 'traceback', 'meta')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskState
        fields = ('state', 'task_id', 'name', 'tstamp', 'args',
                  'kwargs', 'eta', 'expires', 'result', 'traceback', 'runtime',
                  'retries', 'worker', 'hidden')


class TaskwithCustomTaskNameSerializer(serializers.ModelSerializer):
    taskstate = TaskSerializer()

    class Meta:
        model = TaskwithCustomTaskName
        fields = ('custom_task_name', 'taskstate')

    def create(self, validated_data):
        taskstate_data = validated_data.pop('taskstate')
        task_custom_taskname = TaskwithCustomTaskName.objects.create(**validated_data)
        TaskState.objects.create(task_custom_taskname=task_custom_taskname, **taskstate_data)

    def update(self, instance, validated_data):
        taskstate_data = validated_data.pop('taskstate')
        taskstate = instance.taskstate

        instance.custom_taskname = validated_data.get('custom_task_name', instance.custom_task_name)
        instance.save()

        taskstate.update(taskstate, taskstate_data)
        taskstate.save()

        return instance