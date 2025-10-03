from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Author, Book
from django.contrib.auth.models import User

class BookAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="pass123")
        self.author = Author.objects.create(name="Author A")
        self.book = Book.objects.create(title="Book A", publication_year=2020, author=self.author)

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.data, status.HTTP_200_OK)

    def test_create_book_authenticated(self):
        self.client.login(username="tester", password="pass123")
        url = reverse('book-list')
        data = {"title": "New Book", "publication_year": 2021, "author": self.author.id}
        response = self.client.post(url, data)
        self.assertEqual(response.data, status.HTTP_201_CREATED)

    def test_create_book_unauthenticated(self):
        url = reverse('book-list')
        data = {"title": "Fail Book", "publication_year": 2021, "author": self.author.id}
        response = self.client.post(url, data)
        self.assertEqual(response.data, status.HTTP_403_FORBIDDEN)

    def test_filter_books(self):
        url = reverse('book-list') + '?search=Book'
        response = self.client.get(url)
        self.assertEqual(response.data, status.HTTP_200_OK)
