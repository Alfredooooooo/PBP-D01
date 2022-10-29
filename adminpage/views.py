from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime 
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from adminpage.forms import TaskForm
from adminpage.models import TaskAdmin
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
@login_required(login_url='/adminpage/login/') # Merestriksi akses halaman adminpage
def show_adminpage(request):
    username = request.user.username
    user_id = request.user.id
    tasks = TaskAdmin.objects.filter(user_id=user_id)
    context = { 
        "username": username,
        "adminpage": tasks
    }
    return render(request, "adminpage.html", context)

def registrasi_user(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful")
            return redirect("adminpage:login_user")
    context = {"form":form}
    return render(request, "registration.html", context)

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("adminpage:show_adminpage")
    context = {}
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    return redirect("adminpage:login_user")

@login_required(login_url='/adminpage/login/') # Merestriksi akses halaman create-task
def create_task(request):
    if request.method == "POST":
        judul = request.POST.get("judul")
        deskripsi = request.POST.get("deskripsi")
        newTask = TaskAdmin(user=request.user, title=judul, description=deskripsi, date=datetime.now())
        newTask.save()
        return redirect("adminpage:show_adminpage")
    return render(request, "create_task.html")

@login_required(login_url='/adminpage/login/')
def delete_task(request, id):
    task = TaskAdmin.objects.get(id=id)
    task.delete()
    return HttpResponseRedirect("/adminpage")

@login_required(login_url='/adminpage/login/')
def update_status(request, id):
    task = TaskAdmin.objects.get(id=id)
    if task.user == request.user:
        task.is_finished = not task.is_finished
        task.save()
    return redirect('adminpage:show_adminpage')

@login_required(login_url='/adminpage/login/')
def show_adminpage_json(request):
    data = TaskAdmin.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

@login_required(login_url='/adminpage/login/') 
def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        start_date = request.POST.get("start_date")
        finish_date = request.POST.get("finish_date")
        task = TaskAdmin.objects.create(
            user=request.user,
            title=title, 
            description=description,
            date=datetime.now(),
            start_date=start_date,
            finish_date=finish_date,
            is_finished=False
        )
        context = {
            'pk':task.pk,
            'fields':{
                'title':task.title,
                'description':task.description,
                'date':task.date,
                'start_date':task.start_date,
                'finish_date':task.finish_date,
                'is_finished':task.is_finished,
            }
        }
    return JsonResponse(context)

@login_required(login_url='/adminpage/login/')
def submit_ajax(request):
    print(request.POST.get('new_event'))
    if request.method == 'POST':
        new_event = request.POST.get('new_event')
        title = request.POST.get('title')
        description = request.POST.get('description')
        new_event = TaskAdmin(title=title, description=description)
        new_event.save()
        return HttpResponseRedirect('/adminpage/ajax/')
    return HttpResponse('Selamat, berhasil dikirim!')