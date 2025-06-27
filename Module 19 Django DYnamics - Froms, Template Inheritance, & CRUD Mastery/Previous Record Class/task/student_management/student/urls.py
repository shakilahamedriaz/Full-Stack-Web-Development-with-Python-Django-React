from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
  #path('home/', views.home, name="home"),  #function based view
  path('home/', views.StudentLists.as_view(), name="home"),  # class based view
  #path('create/', views.create_student, name = "create_student"), #function based view
  path('create/', views.CreateStudent.as_view(), name='create_student'),
  #path('edit/<int:id>/', views.update_student , name = "update_student"), #function based view
  path('edit/<int:id>/', views.StudentUpdate.as_view(), name = "update_student"), #class based view
  #path('delete/<int:id>/', views.delete_student , name = "delete_student"), #function based view
  path('delete/<int:id>/', views.StudentDelete.as_view(), name = "delete_student"), #class based view
  
  path('signup/', views.signup, name = "signup"),
]


