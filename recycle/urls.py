from django.urls import path
from recycle.views import index

app_name = 'recycle'

urlpatterns = [
    path('', index, name='index'),
]
