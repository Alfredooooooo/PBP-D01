from django.db import models
from django.contrib.auth.models import User

## Create your models here.
class AdminPage(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, default =None)
    nama_admin = models.CharField(max_length=50)
    email_admin = models.TextField()
    deskripsi = models.TextField(max_length=50)
