from django.forms import forms
from .import models
# This is for Model Forms
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = '__all__'
        labels = {
            'name': 'Full Name',
            'photo': "Upload Photo",

        }
        help_texts = {
            'email': "Email will be confidential",
        }