from django import forms
from django.forms import ModelForm
from .models import AdminPage
from django.contrib.admin.widgets import AdminSplitDateTime

class TaskForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=150, widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
        }))

    last_name = forms.CharField(label="Last Name", widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
        }))

    email = forms.EmailField(label="Email", widget=forms.TextInput(
    attrs = {
        'class': 'form-control',
    }))


class AdminPageForm(ModelForm):
    class Meta:
        model = AdminPage
        fields = ("nama_admin", "email_admin", "deskripsi")
        widgets = {
            "nama_admin": forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "Nama Admin", "id": "nama-admin",  "rows": "2"}),
            "email_admin": forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "Email Admin", "id": "email-admin", "rows": "2"}),
            "deskripsi": forms.Textarea(attrs={"class": "form-control mb-3", "placeholder": "Deskripsi Admin", "id": "deskripsi-admin", "rows": "2"}),
        }
