from django.forms import forms
from .import models
# This is for Model Forms
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class StudentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
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



class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
