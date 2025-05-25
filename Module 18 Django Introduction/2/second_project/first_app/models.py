from django.db import models

# Create your models here.
#class ---> SQL --> Database e hit korbe

class Blog(models.Model): #database er table hobe
    name = models.TextField()  #field name hobe name


#python manage.py makemigrations : clas -- > sql e convert hobe
# goal hoyce : SQL --> database e kaj korano

#python