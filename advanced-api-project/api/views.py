from rest_framework import generics, viewsets, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# Generic list & detail views for Book (read-only endpoints)
class BookListAPIView(generics.ListAPIView):
    """
    Read-only listing of books. Supports filtering, search, ordering.
    """
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['publication_year', 'author']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']

class BookDetailAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# ViewSet for full CRUD (requires auth for write operations)
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['publication_year', 'author']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']

    def get_permissions(self):
        # Read is allowed for unauthenticated users; write requires authentication
        if self.request.method in ('GET', 'HEAD', 'OPTIONS'):
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.prefetch_related('books').all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]

class AuthorDetailAPIView(generics.RetrieveAPIView):
    queryset = Author.objects.prefetch_related('books').all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]
