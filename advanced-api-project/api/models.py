from django.db import models

class Author(models.Model):
    """
    Represents an author. Simple model with a name.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents a book. Each book is linked to an Author via ForeignKey.
    publication_year is an IntegerField.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
