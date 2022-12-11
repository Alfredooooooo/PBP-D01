from django.shortcuts import render
from adminpage.models import AdminPage
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.core import serializers
from adminpage.forms import TaskForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import TaskForm, AdminPageForm


# Create your views here.
@login_required(login_url="/authentications/login/")
def adminpage(request):
    return render(request, "adminpage.html")

@csrf_exempt
def get_adminpage_json(request):
    adminpage_item = AdminPage.objects.all()
    return HttpResponse(serializers.serialize('json', adminpage_item))

@login_required(login_url="/authentications/login/")
def add_adminpage_item(request):
    if request.method == 'POST':
        nama_admin = request.POST.get("nama_admin")
        email_admin = request.POST.get("email_admin")
        deskripsi = request.POST.get("deskripsi")
        new_data = AdminPage(user=request.user, nama_admin=nama_admin, email_admin=email_admin, deskripsi=deskripsi)
        new_data.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@login_required(login_url="/authentications/login/")
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            
            return render(request, "adminpage.html")
    else:
        form = TaskForm()
    
    context = {'form':form}
    return render(request, "adminpage.html", context)

@csrf_exempt
def add_new_feedback(request):
        if request.method == 'POST':
            form = AdminPageForm(request.POST)
            if form.is_valid():
                print('form valid')
                nw_feedback = form.save(commit=False)
                form.instance.user = request.user
                nw_feedback.save()
                return JsonResponse(
                    {"fields": {"nama_admin": nw_feedback.nama_admin, "email_admin": nw_feedback.email_admin, "deskripsi": nw_feedback.deskripsi}}
                )
            else:
                print("form ga valid")
                return JsonResponse({"status": "Failed make new feedback"})
        else:
            return JsonResponse({"status": "Failed make new feedback"})






