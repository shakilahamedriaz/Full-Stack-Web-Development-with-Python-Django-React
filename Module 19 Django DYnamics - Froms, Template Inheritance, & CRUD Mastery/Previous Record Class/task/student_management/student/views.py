# student management application

# views.py:
# ... (your existing imports)
from django.shortcuts import render, HttpResponse, redirect
from .import models
from . import forms
from django.contrib import messages
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


from django.contrib.auth.mixins import LoginRequiredMixin
# ... (CreateStudent, StudentLists, StudentUpdate, StudentDelete classes are fine) ...
# NOTE: Your Class-Based Views for Create, List, Update, and Delete are well-written and need no changes.
# The function-based views below are also kept for reference or use.

# def create_student(request):
#     if request.method == 'POST':
#         form = forms.StudentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.SUCCESS, 'Student Created successfully.')
#             return redirect('home')
#     else:
#         form = forms.StudentForm()
#     return render(request, 'student/create_edit_student.html', {'form': form})

class CreateStudent(LoginRequiredMixin,CreateView):
    form_class = forms.StudentForm
    success_url = reverse_lazy('home')
    template_name = 'student/create_edit_student.html'

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Student Created Successfully')
        return super().form_valid(form)


def home(request):
    students = models.Student.objects.all()
    return render(request, 'student/index.html', {'students': students})


class StudentLists(ListView):
    model = models.Student
    template_name = 'student/index.html'
    context_object_name = 'students'


def update_student(request, id):
    student = models.Student.objects.get(id=id)
    form = forms.StudentForm(instance=student)
    if request.method == 'POST':
        form = forms.StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Student Updated successfully.')
            return redirect('home')
    return render(request, 'student/create_edit_student.html', {'form': form, 'edit': True})


class StudentUpdate(LoginRequiredMixin,UpdateView):
    model = models.Student
    form_class = forms.StudentForm
    template_name = 'student/create_edit_student.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
    
    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Student Updated successfully.')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit'] = True
        return context


def delete_student(request, id):
    student = models.Student.objects.get(id=id)
    student.delete()
    messages.add_message(request, messages.SUCCESS, 'Student Deleted successfully.')
    return redirect('home')


class StudentDelete(DeleteView):
    model = models.Student
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')
    template_name = 'student/delete_student.html'

    def form_valid(self, form):
        # Overriding form_valid to add a message, as DeleteView doesn't call it by default.
        # A better place is the delete() method as you correctly did.
        # This is just for info, your original code was correct.
        return super().form_valid(form)
        
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Student Deleted successfully.')
        return super().delete(request, *args, **kwargs)

def signup(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully. Please Login.')
            return redirect('user_login') # Redirect to login after successful signup
    else:
        form = forms.SignUpForm()
    return render(request, 'student/auth_form.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST) # Pass request to AuthenticationForm
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login Successful')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        # FIX: Removed the redundant 'else' block here. If the form is invalid,
        # Django and Crispy Forms will automatically display the specific errors
        # (e.g., "This field is required.").
    else:
        form = AuthenticationForm()
    return render(request, 'student/auth_form.html', {'form': form, 'type': 'Login'})


# NEW: Added a logout view
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('home')