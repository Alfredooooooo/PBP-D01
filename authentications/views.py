from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render
from django.core import serializers
from recycle.forms import RegisterUserForm
from django.contrib.auth.models import User



def user_type(request):
  if request.method == 'POST':
    form = RegisterUserForm(request.POST)

    if form.is_valid():
      answer = form.cleaned_data['value']
      print(answer)
      if answer == "admin" :
        print(answer)

def register_user(request):
    # Memanggil RegisterUserForm yang merupakan anak dari UserCreationForm
    form = RegisterUserForm()
    if (request.method == "POST"):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(
                request, f"User dengan nama {username} berhasil dibuat")
            user_type(request)
            # Memindahkan url user ke login agar dapat login
            return redirect("authentications:login_user")
        else:
            messages.info(
                request, "Ada yang salah dalam proses Registrasi. Silahkan coba lagi!")
    return render(request, "register.html", {
        "form": form,
    })


def login_user(request):
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
    return render(request, "login.html", {})


def logout_user(request):
    # Melakukan logout
    logout(request)
    response = HttpResponseRedirect(reverse("recycle:index"))
    return response

