# Create - Django shell commands

Run the Django shell:

Create a Book instance:
```py
from bookshelf.models import Book
b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(b)  # Expected: 1984 by George Orwell (1949)
