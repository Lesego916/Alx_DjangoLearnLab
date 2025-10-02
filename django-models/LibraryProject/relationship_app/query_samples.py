from .models import Author, Library

# Query all books by a specific author
def books_by_author(author_name):
    Author.objects.get(name=author_name)
    objects.filter(author=author)
    return Book.objects.filter(author__name=author_name)

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    Librarian.objects.get(library=library_name)
    return library.librarian
