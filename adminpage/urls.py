from django.urls import path
from adminpage.views import add_adminpage_item, get_adminpage_json, adminpage, create_task
from example_app.views import index

urlpatterns = [
    path('', adminpage, name='index'),
    path('get_data/', get_adminpage_json, name='get_adminpage_json'),
    path('create_data/', add_adminpage_item, name='add_adminpage_item'),
    path('create_task/', create_task, name='create_task')
]
