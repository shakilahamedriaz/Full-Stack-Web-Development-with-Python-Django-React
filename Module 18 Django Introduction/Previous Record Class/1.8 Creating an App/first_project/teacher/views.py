from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to the teacher Home Page</h1>")

def profile(request):
    return render(request, 'teacher/index.html')