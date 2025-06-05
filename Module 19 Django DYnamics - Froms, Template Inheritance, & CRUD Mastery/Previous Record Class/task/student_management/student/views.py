from django.shortcuts import render , HttpResponse
from .import models
from . import forms
# Create your views here.

# There are three types of froms in Django
 #HTML Form
 #From Api
 #MODEL Form
  
# This is for HTML Forms
# def home(request):
#     print(request.POST)
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         password = request.POST.get('password')
#         checkbox = request.POST.get('checkbox')
#         photo = request.FILES.get('photo')

#         if checkbox == 'on':
#             checkbox = True
#         else:
#             checkbox = False

#         student = models.Student(
#             name=name,
#             email=email,
#             phone=phone,
#             password=password,
#             checkbox=checkbox,
#             photo=photo
#         ) # student classer ekta object create korlam
#         student.save() #student table ekt record make korlam
#         #return render(request, 'student/student.html')
#         return HttpResponse('Data saved successfully')
    
        
#     return render(request, 'student/index.html')




# This is for Model Forms
def home(request):
    if request.method == 'POST':  #User post requrest korche
        form = forms.StudentForm(request.POST, request.FILES)  #Form er object create korlam / user post request caputre korlam
        if form.is_valid():          # user data valid or not
            form.save()
            return HttpResponse('Data saved successfully') #saved
        
    else:
        form = forms.StudentForm()
    return render(request, 'student/index.html', {'form': form})  #User get request korche
    