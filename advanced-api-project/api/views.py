from rest_framework import generics, permissions
from rest_framework import filters
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
