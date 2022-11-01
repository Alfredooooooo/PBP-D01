from django.urls import path
<<<<<<< HEAD
from recycle.views import index, about_us, objectives, event, login, logout, register, adminpage
=======
from recycle.views import index, about_us, objectives, event, login_user, logout_user, register_user, show_json_by_user, show_json_not_by_user, show_json_all, create_question, edit_question, delete_question
>>>>>>> b2ef0e0e204d5e196d91c8eeb97ff76d878f59b8

app_name = 'recycle'

urlpatterns = [
    path('', index, name='index'),
    path('aboutus/', about_us, name='about-us'),
    path('event/', event, name='event'),
<<<<<<< HEAD
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("register/", register, name="register"),
    path("adminpage/", adminpage, name="adminpage"),
=======
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("register/", register_user, name="register"),
    path("json-question-user/", show_json_by_user, name="jsonuser"),
    path("json-question-notuser/", show_json_not_by_user, name="jsonnotuser"),
    path("json-question-all/", show_json_all, name="jsonall"),
    path("create-question/", create_question, name="createquestion"),
    path("edit-question/<int:id>/", edit_question, name="editquestion"),
    path("delete-question/<int:id>/", delete_question, name="deletequestion")
>>>>>>> b2ef0e0e204d5e196d91c8eeb97ff76d878f59b8
]

