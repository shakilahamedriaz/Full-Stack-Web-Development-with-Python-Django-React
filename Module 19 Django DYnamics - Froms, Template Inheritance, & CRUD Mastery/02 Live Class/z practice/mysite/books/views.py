from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'


class BookCreateView(CreateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'author', 'published_date', 'isbn', 'pages', 'cover_image', 'language']
    success_url = reverse_lazy('book-list')

    def form_valid(self, form):
        messages.success(self.request, 'Book created successfully!')
        return super().form_valid(form)



class BookUpdateView(UpdateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'author', 'published_date', 'isbn', 'pages', 'cover_image', 'language']
    success_url = reverse_lazy('book-list')

    def form_valid(self, form):
        messages.success(self.request, 'Book updated successfully!')
        return super().form_valid(form)



class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book-list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Book deleted successfully!')
        return super().delete(request, *args, **kwargs)
