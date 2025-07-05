from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),      # for /
    path('home/', views.home, name='home'), # for /home/
]