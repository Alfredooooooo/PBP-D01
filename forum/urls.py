from django.urls import path
from forum.views import *

app_name = 'forum'

urlpatterns = [
    path('<int:id>/', show_forum, name='show_forum'),
    path('json/<int:id>/', get_comments_json, name='get_comments_json'),
    path('json/event/<int:id>/', get_event_json, name='get_event_json'),
    path('add/<int:id1>/<int:id2>/', add_comment, name='add_comment'),
    path('delete/<int:id>/', delete_comment, name='delete_comment'),
    path('username/', get_username, name='get_username'),
]