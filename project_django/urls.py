"""project_django URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recycle.urls')),
<<<<<<< HEAD
    path('event/',include('event.urls')),
    path('forum/', include('forum.urls'))
=======
    path('forum/', include('forum.urls')),
    path('adminpage/', include('adminpage.urls')),
>>>>>>> 893a5dd1786cd5e569117048324a91b33fd4d98b
]

# TODO: Implement Routings Here