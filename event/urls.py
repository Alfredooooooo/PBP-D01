from django.urls import path
from event.views import *

app_name = 'event'

urlpatterns = [
    path('', event_user, name="home"),
    path('user/', event_user, name='user'),
    path('manager/', event_manager, name='manager'),
    path("json-manager/", show_event_manager, name="json-manager"),
    path("json-recent/", show_recently_viewed_event, name="json-recent"),
    path("json-past/", show_past_event, name="json-past"),
    path("json-now/", show_now_event, name="json-now"),
    path("json-upcoming/", show_upcoming_event, name="json-upcoming"),
    path("show/<int:pk>/", show_detail_event, name="show-detail"),
    path('add-event/', add_new_event, name='add-event'),
    path('delete-event/<int:pk>/', delete_event, name='delete-event'),

]
