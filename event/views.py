from ctypes import pointer
from datetime import datetime
from itertools import product
from multiprocessing import context
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
from .forms import EventForm
from django.contrib.auth import get_user_model



@csrf_exempt
def index(request):
    form = EventForm()
    context={
        "form": form
    }
    return render(request, "show-event.html", context)

@csrf_exempt
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
    
@csrf_exempt
def show_detail_event(request, pk):
    global pointer 
    if request.method == 'GET':
        data_event = Event.objects.filter(pk=pk)
        if 'recently_viewed' in request.session:
            if pk not in request.session['recently_viewed']:
                # pointer_session = request.session.get('pointer')
                request.session['recently_viewed'].insert(0, pk)
                # pointer = (pointer + 1) % 3
                # request.sesion['pointer'] = pointer_session

                # request.session['recently_viewed'].insert(0, pk)
                if len(request.session['recently_viewed'])>3:
                    request.session['recently_viewed'].pop()
        else:
            request.session['recently_viewed']=[pk]
            pointer=1

        request.session.modified = True
        return HttpResponse(serializers.serialize("json", data_event), content_type="application/json")
    else:
        data_event = Event.objects.filter(pk=pk)
        return HttpResponse(serializers.serialize("json", data_event), content_type="application/json")

@csrf_exempt
def show_all_event(request):
    if request.method == "GET":
        data_event = Event.objects.all()
        return HttpResponse(serializers.serialize("json", data_event), content_type="application/json")

@csrf_exempt
def show_your_event(request):
    if request.method == "GET":
        data_event = Event.objects.filter(user=request.user)
        return HttpResponse(serializers.serialize("json", data_event), content_type="application/json")

@csrf_exempt
def show_your_event_flutter(request, pk):
    if request.method == "GET":
        data_event = Event.objects.filter(user=pk)
        return HttpResponse(serializers.serialize("json", data_event), content_type="application/json")

@csrf_exempt
def show_ongoing_event(request):
    if request.method == "GET":
        data_event = Event.objects.filter(finish_date__gt=datetime.now()).exclude(start_date__gt=datetime.now())
        return HttpResponse(serializers.serialize("json", data_event), content_type="application/json")

@csrf_exempt
def show_past_event(request):
    if request.method == "GET":
        data_event = Event.objects.filter(finish_date__lt=datetime.now())
        return HttpResponse(serializers.serialize("json", data_event), content_type="application/json")

@csrf_exempt
def show_upcoming_event(request):
    if request.method == "GET":
        data_event = Event.objects.filter(start_date__gt=datetime.now())
        return HttpResponse(serializers.serialize("json", data_event), content_type="application/json")
@csrf_exempt
def show_event_manager(request):
    data_event = Event.objects.all()
    return HttpResponse(serializers.serialize("json", data_event), content_type="application/json")

@csrf_exempt
def add_new_event(request):
    if (request.method == "POST"):
        form = EventForm(request.POST)
        if (form.is_valid()):
            print("ini 1")
            eventBaru = form.save(commit=False)
            form.instance.user = request.user
            eventBaru.save()
            return JsonResponse({"fields":{
                "create_date": eventBaru.create_date,
                "start_date": eventBaru.start_date,
                "finish_date": eventBaru.finish_date,
                "title": eventBaru.title,
                "description": eventBaru.description,
                "brief": eventBaru.brief,
            }})
            
        else:
            print("ini 2")
            return JsonResponse({"status": "Failed makew new event"})
    else:
        return JsonResponse({"status": "Failed makew new event"})


@csrf_exempt
def delete_event(request, pk):
    if request.method == 'DELETE':
        event = Event.objects.get(pk=pk)
        event.delete() 
        return JsonResponse({"status": "Success delete event"},status=200)
    else:
        return JsonResponse({"status": "Failed delete event"},status=403)


@csrf_exempt
def get_user_data(request, pk):
    User = get_user_model()
    user = User.objects.filter(id=pk)
    return HttpResponse(serializers.serialize("json", user), content_type="application/json")
