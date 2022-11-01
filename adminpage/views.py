from django.shortcuts import render
from adminpage.models import BarangWishlist
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from adminpage.forms import TaskForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def wishlist(request):
    return render(request, "adminpage.html")

def get_wishlist_json(request):
    wishlist_item = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize('json', wishlist_item))

def add_wishlist_item(request):
    if request.method == 'POST':
        nama_barang = request.POST.get("nama_barang")
        harga_barang = request.POST.get("harga_barang")
        deskripsi = request.POST.get("deskripsi")
        new_barang = BarangWishlist(nama_barang=nama_barang, harga_barang=harga_barang, deskripsi=deskripsi)
        new_barang.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid(): # Kondisi data pada field valid
            task = BarangWishlist(
                nama_barang = form.cleaned_data['nama_barang'], 
                deskripsi = form.cleaned_data['deskripsi'],
            )
            task.save() # Menyimpan task ke database
            return HttpResponseRedirect(reverse("adminpage:adminpage"))
    else:
        form = TaskForm()
    
    context = {'form':form}
    return render(request, "adminpage.html", context)
