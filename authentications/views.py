from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render
from django.core import serializers
from recycle.forms import RegisterUserForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


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
            # Memindahkan url user ke login agar dapat login
            return redirect("authentications:login_page")
        else:
            messages.info(
                request, "Ada yang salah dalam proses Registrasi. Silahkan coba lagi!")
    return render(request, "register.html", {
        "form": form,
    })


@csrf_exempt
def login_page(request):
    if (request.user.is_authenticated):
        return redirect("recycle:index")
    return render(request, "login.html", {})


@csrf_exempt
def login_user(request):
    data = {}
    if request.method == "POST":
        # Get the username and password from name attribute in input tag
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            data["status"] = True
            data["message"] = "Successfully Logged In!"
            data["username"] = user.username
            data['idUser'] = user.id
            data['isSuperuser'] = user.is_superuser
            print(user.id)
            print("sudah mengembalikan")
            return JsonResponse(data)
        else:
            data["status"] = False
            data["message"] = "Failed to Login, check your email/password."
            return JsonResponse(data)
    else:
        return JsonResponse(data)


def logout_user(request):
    # Melakukan logout
    logout(request)
    response = HttpResponseRedirect(reverse("recycle:index"))
    return response


@csrf_exempt
def logout_user_async(request):
    logout(request)
    return JsonResponse({
        "message": "successfully logged out"
    })
