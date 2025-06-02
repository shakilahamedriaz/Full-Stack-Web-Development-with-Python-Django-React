from django.shortcuts import render

# Create your views here.

# There are three types of froms in Django
 #HTML Form
 #From Api
 #MODEL Form
  

def home(request):
    print(request.POST)
    return render(request, 'student/index.html')