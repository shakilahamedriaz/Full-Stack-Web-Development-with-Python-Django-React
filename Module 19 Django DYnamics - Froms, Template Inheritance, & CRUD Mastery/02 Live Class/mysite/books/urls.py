from django.contrib import admin
from django.urls import path
from .views import BookListView, BookCreateView, BookUpdatedView, BookDeleteView

urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('create/', BookCreateView.as_view(), name='create-book'),  # ✅ Fixed
    path('update/<int:pk>/', BookUpdatedView.as_view(), name = 'update-book'),
    path('delete/<int:pk>/', BookDeleteView.as_view(), name='delete-book'),
]
