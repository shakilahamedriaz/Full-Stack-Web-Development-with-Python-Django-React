from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('task_list'), name='root_redirect'),
    path('admin/', admin.site.urls),
    path('tasks/', include('task.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Add Django auth URLs
]
