from django import forms

class TaskForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=150)
    last_name = forms.CharField(label="Last Name", max_length=150)
    email = forms.EmailField()
