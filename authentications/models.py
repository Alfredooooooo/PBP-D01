from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    status = models.CharField(max_length = 255, default = "user")