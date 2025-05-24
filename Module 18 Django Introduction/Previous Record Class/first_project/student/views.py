from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def profile(request):
    return HttpResponse("I am in Student Profile")


def home(reuest):
    return HttpResponse("I am home page bhai")