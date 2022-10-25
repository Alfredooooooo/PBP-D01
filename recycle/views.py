from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from recycle.forms import RegisterUserForm


def index(request):
    return render(request, 'index.html')


def about_us(request):
    return render(request, 'about-us.html')


def objectives(request):
    return render(request, 'objectives.html')


def event(request):
    return render(request, 'event.html')


def register(request):
    # Memanggil RegisterUserForm yang merupakan anak dari UserCreationForm
    form = RegisterUserForm()
    if (request.method == "POST"):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(
                request, f"User dengan nama {username} berhasil dibuat")
            # Memindahkan url user ke login agar dapat login
            return redirect("recycle:login")
        else:
            messages.info(
                request, "Ada yang salah dalam proses Registrasi. Silahkan coba lagi!")
    return render(request, "authentication/register.html", {
        "form": form,
    })


def login(request):
    # Find POST method
    if request.method == "POST":
        # Get the username and password from name attribute in input tag
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(
                reverse("recycle:index"))  # membuat response
            return response
        else:
            messages.info(request, "Username atau Password salah!")
    return render(request, "authentication/login.html", {})


def logout(request):
    # Melakukan logout
    logout(request)
    response = HttpResponseRedirect(reverse("register:login"))
    return response
