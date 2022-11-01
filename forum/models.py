from django.db import models
from django.contrib.auth.models import User
from event.models import Event
from django.utils import timezone

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    username = models.TextField()
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True)
    parent_pk = models.IntegerField(null=True)
    parent_username = models.TextField(null=True)
    datetime = models.DateTimeField(default=timezone.now)
    comment_text = models.TextField()