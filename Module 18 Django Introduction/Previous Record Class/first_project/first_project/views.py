from django.http import HttpResponse

def home(reuest):
    print("Hello Im Here!!")
    return HttpResponse("<h1>Hellow eibar ok<h1>")