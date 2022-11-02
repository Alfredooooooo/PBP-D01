from django.urls import path
from aboutus.views import aboutus
from example_app.views import index

urlpatterns = [
    path('', aboutus, name='aboutus'),
]