from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.author = Author.objects.create(name='John Doe')
        self.book = Book.objects.create(title='Test Book', publication_year=2020, author=self.author)

    def test_list_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book_requires_auth(self):
        data = {'title': 'New Book', 'publication_year': 2023, 'author': self.author.id}
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='password123')
        data = {'title': 'Auth Book', 'publication_year': 2023, 'author': self.author.id}
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        self.client.login(username='testuser', password='password123')
        data = {'title': 'Updated Title', 'publication_year': 2021, 'author': self.author.id}
        response = self.client.put(f'/api/books/{self.book.id}/update/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.delete(f'/api/books/{self.book.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
