# Retrieve - Django shell commands

Open shell:

Retrieve created book(s):
```py
from bookshelf.models import Book
books = Book.objects.all()
for book in books:
    print(book.title, book.author, book.publication_year)
# Expected output (example): 1984 George Orwell 1949
