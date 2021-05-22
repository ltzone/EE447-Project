from django.db import models

# Create your models here.

class TaskName(models.Model):
    custom_task_name = models.CharField(max_length=200, default="default_name")
    task_id = models.CharField(max_length=200)