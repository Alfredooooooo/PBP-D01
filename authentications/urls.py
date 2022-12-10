from django.urls import path
from authentications.views import *

app_name = 'authentications'

urlpatterns = [
    # path('', index, name='index'),
    path("register/", register_user, name="register_user"),
    path("login/", login_page, name="login_page"),
    path("login/process-login/", login_user, name="login_user"),
    path("logout/", logout_user_async, name="logout_user"),
]
