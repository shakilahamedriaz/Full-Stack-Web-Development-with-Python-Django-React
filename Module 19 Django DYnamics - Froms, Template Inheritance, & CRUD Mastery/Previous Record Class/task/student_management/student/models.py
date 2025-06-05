from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=100) 
    checkbox = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='student/photos/', default=None, null=True)

    def __str__(self):
        return self.name
    
    
