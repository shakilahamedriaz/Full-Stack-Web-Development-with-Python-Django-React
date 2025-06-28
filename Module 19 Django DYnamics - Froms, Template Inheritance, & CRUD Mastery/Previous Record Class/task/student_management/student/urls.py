# urls.py

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('', views.StudentLists.as_view(), name="home"), # Set home as the root URL
  path('home/', views.StudentLists.as_view(), name="home"),
  path('create/', views.CreateStudent.as_view(), name='create_student'),
  path('edit/<int:id>/', views.StudentUpdate.as_view(), name = "update_student"),
  path('delete/<int:id>/', views.StudentDelete.as_view(), name = "delete_student"),
  
  path('signup/', views.signup, name = "signup"),
  path('login/', views.user_login, name = "user_login"),
  path('logout/', views.user_logout, name = "user_logout"), # NEW: Added logout URL
]