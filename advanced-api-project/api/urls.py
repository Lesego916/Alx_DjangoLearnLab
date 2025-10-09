from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BookListAPIView, BookDetailAPIView,
    BookViewSet,
    AuthorListCreateAPIView, AuthorDetailAPIView
)

router = DefaultRouter()
# Register viewset for full CRUD under /books_all/
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Generic list and detail endpoints (read-only)
    path('books/', BookListAPIView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),

    # Author endpoints
    path('authors/', AuthorListCreateAPIView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorDetailAPIView.as_view(), name='author-detail'),

    # Router-managed CRUD endpoints
    path('', include(router.urls)),
]
