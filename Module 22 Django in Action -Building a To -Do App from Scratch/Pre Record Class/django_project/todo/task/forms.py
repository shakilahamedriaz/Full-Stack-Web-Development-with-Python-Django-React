from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['user'] # Exclude the user field from the form, as it will be set automatically