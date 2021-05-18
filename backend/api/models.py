from django.db import models

# Create your models here.

class TaskName(models.Model):
    task_name = models.CharField(max_length=200)
    task_id = models.CharField(max_length=200)