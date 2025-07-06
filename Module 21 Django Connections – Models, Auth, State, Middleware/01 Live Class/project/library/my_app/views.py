from django.shortcuts import render
from django.http import HttpResponse
from .import models
from django.db import models
from django.db.models import Count
from .models import Book, Author


# Create your views here.

def home(request):

    # 1 to Many Relationship

    # books = models.Book.objects.all() # 1 ta SQL Query
    # for book in books:    #N ta SQL Query
    #     print(book.name, book.author.name)

    #Time Complexity: O(N+1) where N is the number of books, that is not Good


    #Selector is used to fetch related objects in a single query
    #one to many relationship er jonno prefetch_related use kora hoy
    books = models.Book.objects.prefetch_related('author') # 1 ta SQL Query, JOIN
    # Time Complexity: O(1) for prefetch_related, O(N) for iter
    for book in books:
        print(book.name, book.author.name)


    # #Many to Many Relationship
    # students = models.Student.objects.all() # 1 ta SQL Query, JOIN
    # for student in students:
    #     print(student.user, [course.name for course in student.courses.all()]) #N ta SQL Query
    # # N+1 query problem is solved by using select_related for one to one and many to one relationships, and prefetch_related for many to many relationships.

    #prefetch_related
    students = models.Student.objects.prefetch_related('courses') # 1 ta SQL Query, JOIN
    for student in students:
        print(student.user, [course.name for course in student.courses.all()])
    # Time Complexity: O(1) for prefetch_related, O(N) for iter

    return HttpResponse("<h1>Welcome to the Library</h1>")



# #model inheritaance
# class commmonInfo(models.Model): #commmonInfo is a base class for other models
#     name = models.CharField(max_length=100)
#     email = models.EmailField()

#     class Meta:
#         abstract = True  # abstract model, not a table in the database
#         #used to define common fields for other models,


# class Owner(commmonInfo):   # Owner model inherits from commmonInfo , now Owner will have name and email fields
#     address = models.CharField(max_length=100)
 
#     def __str__(self):
#         return self.name




#aggrigation vs annotation , example

#aggrigation is used to calculate a single value from a set of values, while annotation is used to add a new field to each object in a queryset.
#aggregation: without grouping, single row
def book_count(request):
    return Book.objects.aggregate(count=Count('id'))
    # this will return a dictionary with count field
    # e.g. {'count': 5} if there are 5 books in the database



#annotation: with grouping, multiple rows
def author_book_count(request):
    return Author.objects.annotate(book_count=Count('book')).values('name', 'book_count')
    # this will return a queryset of dictionaries with name and book_count fields
    # e.g. [{'name': 'Author 1', 'book_count': 2}, {'name': 'Author 2', 'book_count': 3}]



#order by
# def ordered_books(request):
#     return Book.objects.order_by('name')  # Order books by name in ascending order
#     # this will return a queryset of books ordered by name in ascending order
#     # e.g. [Book(name='A Book'), Book(name='B Book'), Book(name='C Book')]

     

# #advanced queries
# def advanced_queries(request):
#     # Get books with more than 2 authors
#     books_with_multiple_authors = Book.objects.annotate(author_count=Count('author')).filter(author_count__gt=2)
#     return books_with_multiple_authors

#     # Get authors who have written more than 3 books
#     authors_with_many_books = Author.objects.annotate(book_count=Count('book')).filter(book_count__gt=3)
#     return authors_with_many_books


#__icontain
# def search_books(request, query):
#     # Search for books with a name that contains the query (case-insensitive)
#     return Book.objects.filter(name__icontains=query)
#     # this will return a queryset of books with names containing the query