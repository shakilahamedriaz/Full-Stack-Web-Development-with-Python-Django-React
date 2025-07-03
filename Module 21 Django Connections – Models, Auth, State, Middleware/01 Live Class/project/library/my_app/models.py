from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

# one to many: one author -- many books
class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# one to one: one user -- one profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.user.username
    


class Course(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)
    #coursename = model relationship( # course er sathe many to many relationship thakbe)

    def __str__(self):
        return self.user.username






## model relationship: all cases given below

#1  ekjon user er ektai account/profile thakbe 
         #(User theke profile er one to one relationship)  I mean user-model er sathe profile-model er one to one relationship thakbe,


#2 ekhon user chaile multiple post likhte parebe,
         # (user er sathe post er one to many relationship thakbe)  I mean user-model er sathe post-model er one to many relationship thakbe,


#3 ekjon user chaile multiple course korte parbe,
   #ekta course e multiple student thakte parbe 
         #(user er sathe course er many to many relationship thakbe)  I mean user-model er sathe course-model er many to many relationship thakbe,


# | Relation       | Example                   | Relation Type |
# | -------------- | ------------------------- | ------------- |
# | User - Profile | 1 User = 1 Profile        | One to One    |
# | User - Post    | 1 User = Many Posts       | One to Many   |
# | User - Course  | Many Users = Many Courses | Many to Many  |
