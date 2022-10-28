from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskAdmin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField()
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()
    title = models.CharField(max_length=150)
    description = models.TextField()
    is_ended = models.BooleanField(default=False)