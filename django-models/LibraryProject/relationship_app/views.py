# Create your views here.
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# List all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

# Detail of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
