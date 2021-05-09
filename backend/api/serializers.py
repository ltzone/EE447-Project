from rest_framework import serializers
from django_celery_results.models import TaskResult


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskResult
        fields = ('task_id', 'task_name', 'task_args', 'task_kwargs',
                'status', 'worker', 'content_type', 'content_encoding',
                'result', 'date_created', 'date_done', 'traceback', 'meta')