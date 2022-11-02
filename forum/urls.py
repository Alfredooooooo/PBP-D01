from django.urls import path
from forum.views import show_forum, get_comments_json, add_comment, delete_comment

app_name = 'forum'

urlpatterns = [
    path('<int:id>/', show_forum, name='show_forum'),
    path('json/<int:id>/', get_comments_json, name='get_comments_json'),
    path('add/<int:id1>/<int:id2>/', add_comment, name='add_comment'),
    path('delete/<int:id>/', delete_comment, name='delete_comment'),
]