import os
from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=100) 
    checkbox = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='student/photo/', default=None, blank=True, null=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    
