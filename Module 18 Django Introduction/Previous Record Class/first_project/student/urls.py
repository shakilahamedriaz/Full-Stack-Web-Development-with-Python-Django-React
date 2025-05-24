from django.urls import path
from .import views


#from views import views

urlpatterns = [
    path('profile/', views.profile),
    path('home/', views.home),


]