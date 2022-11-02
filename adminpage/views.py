from django.shortcuts import render
from adminpage.models import AdminPage
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from adminpage.forms import TaskForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/recycle/login')
def wishlist(request):
    return render(request, "adminpage.html")

@login_required(login_url='/recycle/login')
def get_wishlist_json(request):
    wishlist_item = AdminPage.objects.all()
    return HttpResponse(serializers.serialize('json', wishlist_item))

@login_required(login_url='/recycle/login')
def add_wishlist_item(request):
    if request.method == 'POST':
        nama_admin = request.POST.get("nama_admin")
        email_admin = request.POST.get("email_admin")
        deskripsi = request.POST.get("deskripsi")
        new_data = AdminPage(user=request.user, nama_admin=nama_admin, email_admin=email_admin, deskripsi=deskripsi)
        new_data.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@login_required(login_url='/recycle/login')
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            
            return render(request, "adminpage.html")
    else:
        form = TaskForm()
    
    context = {'form':form}
    return render(request, "adminpage.html", context)


