from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages



# Create your views here.
# Function based view
def home(request):
    books = Book.objects.all() #model
    return render(request, '', {'books': books}) #template name



#Class based view @much better then this
class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author']
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book-list')

    def form_valid(self, form):  # ✅ Correct method name
        messages.success(self.request, '✅ Book Created Successfully!')
        return super().form_valid(form)



class BookUpdatedView(UpdateView):
    model = Book
    fields = ['title', 'author']
    template_name = 'books/book_update.html'
    success_url = reverse_lazy('book-list')

    def form_valid(self, form):  # ✅ Correct method name
        messages.success(self.request, '✅ Book Updated Successfully!')
        return super().form_valid(form)



class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book-list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, '🗑️ Book deleted successfully!')
        return super().delete(request, *args, **kwargs)