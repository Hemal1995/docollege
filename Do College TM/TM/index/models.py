from django.db import models
from setuptools import Require

# Create your models here.
class student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    course = models.CharField(max_length=15)
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    time_minute = models.CharField(max_length=15)