
from django.urls import path, include
from .import views

urlpatterns = [
    path('home/', views.home, name = "home_x"),
    path('profile/', views.profile),

]

# student/profile
# student/home
# student/account