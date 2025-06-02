from django.shortcuts import render
from django.http import HttpResponse
from .import models

# Create your views here.
# def profile(reqquest):
#     return HttpResponse("<h1>Welcome to the Student Profile Page</h1>")


def home(request):
    return HttpResponse("<h1>Welcome to the Student Home Page</h1>")


def account(request):
    return HttpResponse("<h1>Welcome to the Student Account Page</h1>")


def profile(request):
    user_data = {
        'name': 'Shakil',
        'age': 22,
        'email': 'shakil@example.com'
    }

    marks = [
        {
            "id": 1,
            "subject": "Math",
            "marks": 80
        },
        {
            "id": 2,
            "subject": "Physics",
            "marks": 72
        },
        {
            "id": 3,
            "subject": "Machine Learning",
            "marks": 55
        },
        {
            "id": 4,
            "subject": "Data Science",
            "marks": 75
        }
        
    ]

    context = {
        'user_data': user_data,
        'marks': marks,
        'age': 20,
        'Name': "Shakil Ahamed",
        'lst': ["apple", "orange", "banana"]
    }

    student_data = models.Student.objects.all()
    print(student_data)
    return render(request, 'student/index.html', context)


def profile(request):
    return render(request, 'teacher/index.html')    

