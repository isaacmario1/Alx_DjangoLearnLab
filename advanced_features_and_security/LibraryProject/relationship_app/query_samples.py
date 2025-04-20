from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "George Orwell"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print("Books by George Orwell:", books_by_author)

# List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print("Books in Central Library:", books_in_library)

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print("Librarian for Central Library:", librarian.name)
