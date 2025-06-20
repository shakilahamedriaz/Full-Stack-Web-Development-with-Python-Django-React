from django.shortcuts import render , HttpResponse, redirect
from .import models
from . import forms
from django.contrib import messages
from django.views.generic import CreateView, ListView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.views.generic import DeleteView
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
            messages.add_message(request, messages.SUCCESS, 'Student Created successfully.')
            return redirect('home') #saved
            
        
    else:
        form = forms.StudentForm()
    return render(request, 'student/create_edit_student.html', {'form': form}) 

#class view
class CreateStudent(CreateView):
    form_class = forms.StudentForm
    success_url = reverse_lazy('home')
    template_name = 'student/create_edit_student.html'

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Student Created Successfully')
        return super().form_valid(form)


#for function based view for listing students
def home(request):
    students = models.Student.objects.all()  #All data fetch korlam
    return render(request, 'student/index.html', {'students': students})  #data ke template e pathalam


#for class based view for listing students
class StudentLists(ListView):
    model = models.Student
    template_name = 'student/index.html'
    context_object_name = 'students'


#this function based view is for updating student data
def update_student(request, id):
    student = models.Student.objects.get(id=id)
    form = forms.StudentForm(instance=student)  # user er ager data diye form fill up korlam
    # form = forms.StudentForm

    if request.method == 'POST':  # 1. user post request koreche
        form = forms.StudentForm(request.POST, request.FILES, instance=student)  # 2. user er post data & file ashche
        if form.is_valid():  # 3. user input validation kortechi
            form.save()  # 4. user input save korlam
            messages.add_message(request, messages.SUCCESS, 'Student Updated successfully.')
            return redirect('home')

    return render(request, 'student/create_edit_student.html', {'form': form, 'edit': True})

#class based view for updating student data
class StudentUpdate(UpdateView):
    model = models.Student
    form_class = forms.StudentForm
    template_name = 'student/create_edit_student.html'
    success_url = reverse_lazy('home')  #successfully update hoyeche bole home page e redirect korlam
    pk_url_kwarg = 'id'  #URL theke id capture korar jonno
    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Student Updated successfully.')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit'] = True
        return context


#this function based view is for deleting student data
def delete_student(request, id):
    student = models.Student.objects.get(id=id) #id = id wala student ke amra khuje ber korlam, tar object pelam
    student.delete()  #oi student object ke delete korlam
    messages.add_message(request, messages.SUCCESS, 'Student Delete successfully.')
    return redirect('home') #successfully delete hoyeche bole home page e redirect korlam



# class based view for deleting student data
class StudentDelete(DeleteView):
    model = models.Student
    pk_url_kwarg = 'id'  #URL theke id capture korar jonno
    success_url = reverse_lazy('home')
    template_name = 'student/delete_student.html'

    def delete(self, request, *args, **kwargs):
        messages.add_message(self.request, messages.SUCCESS, 'Student Deleted successfully.')
        return super().delete(request, *args, **kwargs)