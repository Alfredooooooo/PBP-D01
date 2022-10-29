from django.urls import path
from event.views import*

app_name = 'event'

urlpatterns = [
    path('user/', event_user, name='user'),
    path('manager/', event_manager, name='manager'),
    path("json-manager/", show_event_manager, name="json-manager"),
    path('add-event/', add_new_event, name='add-event'),
    path('delete-event/<int:pk>/', delete_event, name='delete-event'),

]
