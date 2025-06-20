from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)  # Ensures email is unique
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # Optional profile picture

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Students"  # This will be used in the admin interface