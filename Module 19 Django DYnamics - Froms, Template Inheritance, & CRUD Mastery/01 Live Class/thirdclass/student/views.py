from django.shortcuts import render


# Create your views here.
def student_list(request):
    #the view will render the student list page
    return render(request, 'student/student_list.html')

