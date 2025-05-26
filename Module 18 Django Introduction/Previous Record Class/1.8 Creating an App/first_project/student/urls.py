from django.urls import path, include
from . import views

urlpatterns = [

    path('profile/', views.profile),
    path('home/', views.home),
    path('account/', views.account),
]