from django.shortcuts import render
from .models import Student

# Create your views here.
def student_list(request):
    # This view will render the student list template
    return render(request, 'students/student_list.html')



def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})