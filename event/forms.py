
from django import forms
from django.forms import ModelForm
from event.models import Event
from django.contrib.admin.widgets import AdminSplitDateTime

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ("title", "brief", "description", "start_date", "finish_date")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "Judul Event", "id": "title",  "rows": "2"}),
            "brief": forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "Deskripsi Singkat Event", "id": "brief", "rows": "2"}),
            "description": forms.Textarea(attrs={"class": "form-control mb-3", "placeholder": "Deskripsi Lengkap Event", "id": "description", "rows": "2"}),
            "start_date": forms.DateTimeInput(attrs={"class": "form-control mb-3", "data-format":"dd/MM/yyyy hh:mm:ss", "type":"datetime-local", "id": "start-date", "rows": "2"}),
            "finish_date": forms.DateTimeInput(attrs={"class": "form-control mb-3", "data-format":"dd/MM/yyyy hh:mm:ss", "type":"datetime-local", "id": "finish-date", "rows": "2"}),
        }
