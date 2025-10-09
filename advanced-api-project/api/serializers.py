from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book instances. Validates that publication_year is not in the future.
    """
    class Meta:
        model = Book
        fields = ('id', 'title', 'publication_year', 'author')

    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class NestedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'publication_year')

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author and includes nested books using NestedBookSerializer.
    """
    books = NestedBookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'books')
