from django.urls import path
from event.views import *

app_name = 'event'

urlpatterns = [
    path('', index, name="home"),
    path("json-all/", show_all_event, name="json-all"),
    path("json-your/", show_your_event, name="json-your"),
    path("json-recent/", show_recently_viewed_event, name="json-recent"),
    path('json-ongoing/', show_ongoing_event, name="json-ongoing"),
    path('json-past/', show_past_event, name="json-past"),
    path('json-upcoming/', show_upcoming_event, name="json-upcoming"),
    path("show/<int:pk>/", show_detail_event, name="show-detail"),
    path('add-event/', add_new_event, name='add-event'),
    path('delete-event/<int:pk>/', delete_event, name='delete-event'),

]
