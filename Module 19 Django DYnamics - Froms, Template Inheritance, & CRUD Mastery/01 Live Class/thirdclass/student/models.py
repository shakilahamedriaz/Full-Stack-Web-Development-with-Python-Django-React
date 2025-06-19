from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)  # Ensure email is unique
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # Optional profile picture
    dob = models.DateField(null=True, blank=True)  # Date of birth
    def __str__(self):
        return self.name

