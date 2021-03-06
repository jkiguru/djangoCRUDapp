from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    task_name = models.CharField(max_length=255)
    task_desc = models.TextField(blank=True)
    task_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    task_taker = models.CharField(max_length=255, blank=True)
    time_created = models.DateTimeField(default=timezone.now)
    time_taken = models.DateTimeField(blank=True, null=True)
    time_done = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.id} - {self.task_name}'
class Lecturer(models.Model):
    section = models.CharField(max_length=255)
    instructor = models.CharField(max_length = 255)
    Title = models.CharField(max_length=255)
    id = models.BigAutoField(primary_key=True)
    class Meta:
      verbose_name_plural = "lecturers"

    def __str__(self):
        return self.instructor