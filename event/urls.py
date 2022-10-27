from django.urls import path
from event.views import*

app_name = 'recycle'

urlpatterns = [
    path('user/', event_user, name='user'),
    path('manager/', event_manager, name='manager'),

]
