from django import forms

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