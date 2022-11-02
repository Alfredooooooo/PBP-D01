from django.urls import path
from event.views import *

app_name = 'event'

urlpatterns = [
    path('', event_user, name="home"),
    path('user/', event_user, name='user'),
    path('manager/', event_manager, name='manager'),
    path("json-all/", show_all_event, name="json-all"),
    path("json-your/", show_your_event, name="json-your"),
    path("json-recent/", show_recently_viewed_event, name="json-recent"),
    path("show/<int:pk>/", show_detail_event, name="show-detail"),
    path('add-event/', add_new_event, name='add-event'),
    path('delete-event/<int:pk>/', delete_event, name='delete-event'),

]
