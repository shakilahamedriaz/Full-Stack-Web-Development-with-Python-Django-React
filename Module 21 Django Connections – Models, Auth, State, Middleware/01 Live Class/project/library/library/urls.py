# ...existing code...
from django.urls import path, include

urlpatterns = [
    # ...existing patterns...
    path('', include('my_app.urls')),  # add this line
]