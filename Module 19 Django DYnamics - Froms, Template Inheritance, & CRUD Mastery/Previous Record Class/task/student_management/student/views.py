from django.shortcuts import render , HttpResponse
from .import models
# Create your views here.

# There are three types of froms in Django
 #HTML Form
 #From Api
 #MODEL Form
  

def home(request):
    print(request.POST)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        checkbox = request.POST.get('checkbox')

        if checkbox == 'on':
            checkbox = True
        else:
            checkbox = False

        student = models.Student(
            name=name,
            email=email,
            phone=phone,
            password=password,
            checkbox=checkbox
        ) # student classer ekta object create korlam
        student.save() #student table ekt record make korlam
        #return render(request, 'student/student.html')
        return HttpResponse('Data saved successfully')
    
        
    return render(request, 'student/index.html')