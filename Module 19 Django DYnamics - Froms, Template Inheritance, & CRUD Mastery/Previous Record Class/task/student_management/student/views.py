from django.shortcuts import render , HttpResponse, redirect
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
def create_student(request):
    if request.method == 'POST':  #User post requrest korche
        form = forms.StudentForm(request.POST, request.FILES)  #Form er object create korlam / user post request caputre korlam
        if form.is_valid():          # user data valid or not
            form.save()
            return redirect('home') #saved
            
        
    else:
        form = forms.StudentForm()
    return render(request, 'student/create_edit_student.html', {'form': form}) 

 #User get request korche

def home(request):
    students = models.Student.objects.all()  #All data fetch korlam
    return render(request, 'student/index.html', {'students': students})  #data ke template e pathalam

def update_student(request, id):
    student = models.Student.objects.get(id=id)
    form = forms.StudentForm(instance=student)  # user er ager data diye form fill up korlam
    # form = forms.StudentForm

    if request.method == 'POST':  # 1. user post request koreche
        form = forms.StudentForm(request.POST, request.FILES, instance=student)  # 2. user er post data & file ashche
        if form.is_valid():  # 3. user input validation kortechi
            form.save()  # 4. user input save korlam
            return redirect('home')

    return render(request, 'student/create_edit_student.html', {'form': form, 'edit': True})

    
def update_student(request, id):
    student = models.Student.objects.get(id=id)
    form = forms.StudentForm(instance=student)  # user er ager data diye form fill up korlam
    # form = forms.StudentForm

    if request.method == 'POST':  # 1. user post request koreche
        form = forms.StudentForm(request.POST, request.FILES, instance=student)  # 2. user er post data & file ashche
        if form.is_valid():  # 3. user input validation kortechi
            form.save()  # 4. user input save korlam
            return redirect('home')

    return render(request, 'student/create_edit_student.html', {'form': form, 'edit': True})


def delete_student(request, id):
    student = models.Student.objects.get(id=id) #id = id wala student ke amra khuje ber korlam, tar object pelam
    student.delete()  #oi student object ke delete korlam
    return redirect('home') #successfully delete hoyeche bole home page e redirect korlam
   