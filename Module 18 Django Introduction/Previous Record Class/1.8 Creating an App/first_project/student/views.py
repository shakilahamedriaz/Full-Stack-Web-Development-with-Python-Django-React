from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def profile(reqquest):
    return HttpResponse("<h1>Welcome to the Student Profile Page</h1>")


def home(request):
    return HttpResponse("<h1>Welcome to the Student Home Page</h1>")


def account(request):
    return HttpResponse("<h1>Welcome to the Student Account Page</h1>")