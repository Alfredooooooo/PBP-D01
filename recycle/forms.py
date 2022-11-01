from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from recycle.models import Question


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "Username"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password2"].widget.attrs["placeholder"] = "Retype Password"


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ("title", "description")

        labels = {
            "title": "",
            "description": "",
        }

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "Question Title", "name": "title"}),
            "description": forms.Textarea(attrs={"class": "form-control mb-3", "placeholder": "Question Description", "name": "description", "rows": "2"}),
        }
