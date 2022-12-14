from django.urls import path
from recycle.views import index, adminpage, about_us, event, show_json_by_user, show_json_not_by_user, show_json_all, create_question, edit_question, delete_question

app_name = 'recycle'

urlpatterns = [
    path('', index, name='index'),
    path('aboutus/', about_us, name='about-us'),
    path("adminpage/", adminpage, name="adminpage"),
    path("json-question-user/", show_json_by_user, name="jsonuser"),
    path("json-question-notuser/", show_json_not_by_user, name="jsonnotuser"),
    path("json-question-all/", show_json_all, name="jsonall"),
    path("create-question/", create_question, name="createquestion"),
    path("edit-question/<int:id>/", edit_question, name="editquestion"),
    path("delete-question/<int:id>/", delete_question, name="deletequestion")
]

