from django.urls import path
from wishlist.views import show_wishlist

app_name = 'admin'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
]