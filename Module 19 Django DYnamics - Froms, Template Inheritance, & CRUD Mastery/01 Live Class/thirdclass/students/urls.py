from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),  # Home page
    path('create/', views.student_create, name='student_create'),  # Create student
]
