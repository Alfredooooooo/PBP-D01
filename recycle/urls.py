from django.urls import path
from recycle.views import index, about_us, objectives, event, login, logout, register

app_name = 'recycle'

urlpatterns = [
    path('', index, name='index'),
    path('aboutus/', about_us, name='about-us'),
    path('objectives/', objectives, name='objectives'),
    path('event/', event, name='event'),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("register/", register, name="register"),
]
