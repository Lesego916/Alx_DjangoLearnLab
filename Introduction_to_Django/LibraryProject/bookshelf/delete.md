# Delete - Django shell commands

Open shell:

Delete the book:
```py
from bookshelf.models import Book
b = Book.objects.get(title="Nineteen Eighty-Four")
b.delete()
# Confirm deletion
print(Book.objects.all())  # Expected: <QuerySet []>
