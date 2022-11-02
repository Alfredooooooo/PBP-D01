from django.db import models
from django.contrib.auth.models import User

## Create your models here.
class BarangWishlist(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, default =None)
    nama_barang = models.CharField(max_length=50)
    harga_barang = models.TextField()
    deskripsi = models.TextField(max_length=50)
