# books/urls.py

from django.urls import path
# Import all your views from the views.py file
from .views import BookListView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    # URL for listing all books
    path('', BookListView.as_view(), name='book-list'),

    # URL for creating a new book
    path('create/', BookCreateView.as_view(), name='book-create'),

    # URL for updating an existing book
    # <int:pk> captures the primary key of the book to be updated
    path('<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),

    # URL for deleting an existing book
    # <int:pk> captures the primary key of the book to be deleted
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
