from django.contrib import admin

from forum.models import Comment
from event.models import Event

admin.site.register(Comment)
admin.site.register(Event)
