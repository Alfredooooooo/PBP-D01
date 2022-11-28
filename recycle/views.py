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
from recycle.forms import RegisterUserForm, QuestionForm
from recycle.models import Question

def index(request):
    setCookieIndex(request)
    form = QuestionForm()
    return render(request, 'index.html', {"form": form, "visits": request.session.get("visits")})


def setCookieIndex(request):
    response = HttpResponseRedirect("/recycle/")
    visits = request.session.get('visits', 0)
    request.session['visits'] = visits + 1
    # visits = int(request.COOKIES.get('visits', '0'))
    # print(visits)
    # response.set_cookie('visits', str(visits+4))
    # print("Seriusan", request.COOKIES.get("visits"))
    # return response
    return response

def about_us(request):
    return render(request, 'aboutus.html')

def objectives(request):
    return render(request, 'objectives.html')

def event(request):
    return render(request, 'event.html')

@login_required(login_url="/authentications/login/")
def adminpage(request):
    
    return render(request, 'adminpage.html')


@login_required(login_url="/authentications/login/")
def show_json_by_user(request):
    data = Question.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


@login_required(login_url="/authentications/login/")
def show_json_not_by_user(request):
    data = Question.objects.exclude(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_json_all(request):
    data = Question.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


@csrf_exempt
def create_question(request):
    print("masuk")
    if (request.method == "POST"):
        print("masuk post")
        # Memberikan QuestionForm informasi-informasi yang diberikan pada user setelah user mengisi form
        form = QuestionForm(request.POST)
        if (form.is_valid()):
            questionPost = form.save(commit=False)
            form.instance.user = request.user
            questionPost.save()
            print("GO HERE")
            return JsonResponse({"fields": {
                "user": questionPost.user.username,
                "title": questionPost.title,
                "description": questionPost.description,
                "date": questionPost.date,
                "id": questionPost.id
            }})
        else:
            return JsonResponse({"dt": "whatever"})
    else:
        print("kocak")


@csrf_exempt
def edit_question(request, id):
    print("asdasd")
    objectToBeEdited = Question.objects.get(pk=id)
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if (form.is_valid()):
            objectToBeEdited.title = form.cleaned_data['title']
            objectToBeEdited.description = form.cleaned_data['description']
            print(objectToBeEdited.title, " ", objectToBeEdited.description)
            objectToBeEdited.save()
            return JsonResponse({"fields": {
                "title": objectToBeEdited.title,
                "description": objectToBeEdited.description,
                "date": objectToBeEdited.date,
            }})
        else:
            return JsonResponse({"dt": "whatever"})
    else:
        print("method is not POST")


@csrf_exempt
def delete_question(request, id):
    objectToBeDeleted = Question.objects.filter(pk=id)
    objectToBeDeleted.delete()
    obj = Question.objects.all()
    # listTask = []
    # for t in task:
    #     print(t)
    #     data = {"fields": {
    #         "id": t.get("id"),
    #         "title": t.get("title"),
    #         "description": t.get("description"),
    #         "date": t.get("date"),
    #         "is_finished": t.get("is_finished"),
    #     }}
    #     listTask.append(data)
    return JsonResponse({"data": "whatever"})
