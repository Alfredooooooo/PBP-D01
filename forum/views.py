from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, HttpResponseNotFound
from event.models import Event
from forum.models import Comment
import datetime

def show_forum(request, id):
    data_forum = Event.objects.get(id=id)
    context = {
        'forum_data': data_forum,
        'logged_in': request.user.is_authenticated,
    }
    return render(request, 'forum.html', context)

def get_comments_json(request, id):
    event = Event.objects.get(id=id)
    comments = Comment.objects.filter(event=event)
    return HttpResponse(serializers.serialize('json', comments))

def add_comment(request, id1, id2):
    if request.method == 'POST' and request.user.is_authenticated:
        new_comment = Comment()
        new_comment.user = request.user
        new_comment.username = request.user.username
        new_comment.date = str(datetime.datetime.now())
        new_comment.comment_text = request.POST.get('comment_text')
        if(id2 == 0):
            new_comment.parent = None
        else:
            new_comment.parent = Comment.objects.get(pk=id2)
            new_comment.parent_pk = new_comment.parent.pk
            new_comment.parent_username = new_comment.parent.username
        
        event = Event.objects.get(id=id1)
        new_comment.event = event

        new_comment.save()
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    if request.method == 'POST' and comment.user == request.user:
        comment.delete()
        return HttpResponse(b"DELETED", status=200)

    return HttpResponseNotFound()