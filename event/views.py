from datetime import datetime
from itertools import product
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import *

# Create your views here.
def event_manager(request):
    return render(request, "show-event-manager.html")

def event_user(request):
    return render(request, "show-event-user.html")

def show_recently_viewed_event(request):
    if request.method == 'GET':
        if 'recently_viewed' not in request.session:
            recently_viewed_events = []
            return HttpResponse(serializers.serialize("json", recently_viewed_events), content_type="application/json")
        else:
            recently_viewed_events = Event.objects.filter(pk__in=request.session['recently_viewed'])
            return HttpResponse(serializers.serialize("json", recently_viewed_events), content_type="application/json")
    else:
        recently_viewed_events = []
        return HttpResponse(serializers.serialize("json", recently_viewed_events), content_type="application/json")
    
def show_detail_event(request, pk):
    if request.method == 'GET':
        data_event = Event.objects.filter(pk=pk)
        if 'recently_viewed' in request.session:
            if pk not in request.session['recently_viewed']:
                recently_viewed_events = Event.objects.filter(pk__in=request.session['recently_viewed'])
                request.session['recently_viewed'].insert(0, pk)
                if len(request.session['recently_viewed'])>3:
                    request.session['recently_viewed'].pop()
        else:
            request.session['recently_viewed'] = [pk]
        request.session.modified = True
        return HttpResponse(serializers.serialize("json", data_event), content_type="application/json")
    else:
        data_event = Event.objects.filter(pk=pk)
        return HttpResponse(serializers.serialize("json", data_event), content_type="application/json")

def show_now_event(request):
    if request.method == "GET":
        data_event = Event.objects.filter(start_date__gte=datetime.now, finish_date__lt=datetime.now)
        return HttpResponse(serializers.serialize("json", data_event), content_type="application/json")

def show_past_event(request):
    if request.method == "GET":
        data_event = Event.objects.filter(finish_date__gt=datetime.now)
        return HttpResponse(serializers.serialize("json", data_event), content_type="application/json")

def show_upcoming_event(request):
    if request.method == "GET":
        data_event = Event.objects.get(start_date__gt=datetime.now)
        return HttpResponse(serializers.serialize("json", data_event), content_type="application/json")


def show_event_manager(request):
    data_event = Event.objects.all()
    return HttpResponse(serializers.serialize("json", data_event), content_type="application/json")

@csrf_exempt
def add_new_event(request):
    if request.method == 'POST':
        user=authenticate(request, username="gabriel.zebaoth", password="gabinggaul123")
        start_date = request.POST.get('start_date')
        finish_date = request.POST.get('finish_date')
        title=request.POST.get('title')
        brief=request.POST.get('brief')
        description = request.POST.get('description')
        event = Event(user=user, start_date = start_date, finish_date=finish_date,title=title, brief=brief, description=description)
        event.save()
        return JsonResponse({'status': 'success'}, status=200)
    else:
        return JsonResponse({'status': 'forbidden'}, status=403)

@csrf_exempt
def delete_event(request, pk):
    if request.method == 'DELETE':
        event = Event.objects.get(pk=pk)
        event.delete() 
        return JsonResponse({"status": "Success delete event"},status=200)
    else:
        return JsonResponse({"status": "Failed delete event"},status=403)