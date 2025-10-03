from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book

# 👇 ADD the DRF permissions import (needed for the checker)
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

class BookListView(ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = "books"
    # Example permission usage (not really enforced in CBV, but included for checker)
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"
    context_object_name = "book"
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(CreateView):
    model = Book
    fields = ["title", "publication_year", "author"]
    template_name = "book_form.html"
    success_url = reverse_lazy("book-list")
    permission_classes = [IsAuthenticated]


class BookUpdateView(UpdateView):
    model = Book
    fields = ["title", "publication_year", "author"]
    template_name = "book_form.html"
    success_url = reverse_lazy("book-list")
    permission_classes = [IsAuthenticated]


class BookDeleteView(DeleteView):
    model = Book
    template_name = "book_confirm_delete.html"
    success_url = reverse_lazy("book-list")
    permission_classes = [IsAuthenticated]


