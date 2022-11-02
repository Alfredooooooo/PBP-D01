from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()
    title = models.CharField(max_length=150)
    brief = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self) :
        return self.title