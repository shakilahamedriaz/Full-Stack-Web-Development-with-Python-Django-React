from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Task(models.Model):
    
    STATUS = [
        ('pending', 'Pending'),  # one is for the value and the second is for the display name
        ('completed', 'Completed'),
    ]

    CATEGORY = [
        ('work', 'Work'), 
        ('personal', 'Personal'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    due_time = models.TimeField(blank=True, null=True)
    status = models.CharField(max_length=10, choices= STATUS, default='pending')
    category = models.CharField(max_length=10, choices=CATEGORY)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')


    def __str__(self):  #used to represent the object in the admin panel and shell
        return self.title

