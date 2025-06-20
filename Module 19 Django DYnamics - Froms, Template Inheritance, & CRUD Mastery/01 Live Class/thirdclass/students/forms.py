from django import forms
from .models import Student

class StudentForm(forms.ModelForm):  # Fixed typo here
    class Meta:
        model = Student
        fields = ['name', 'email', 'age', 'profile_pic']  # Changed 'field' to 'fields' and removed trailing comma
