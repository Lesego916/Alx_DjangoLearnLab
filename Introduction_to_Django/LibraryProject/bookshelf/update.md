# Update - Django shell commands

Open shell:

Find & update:
```py
from bookshelf.models import Book
b = Book.objects.get(title="1984")
b.title = "Nineteen Eighty-Four"
b.save()
print(b)  # Expected: Nineteen Eighty-Four by George Orwell (1949)
