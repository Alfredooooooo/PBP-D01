from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/recycle/login')
def aboutus(request):
    return render(request, "aboutus.html")
