from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Author, Book
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class APITests(APITestCase):
    def setUp(self):
        # create a user and token
        self.user = User.objects.create_user(username='tester', password='pass')
        self.token, _ = Token.objects.get_or_create(user=self.user)

        # create sample author and books
        self.author = Author.objects.create(name='Author One')
        self.book = Book.objects.create(title='First Book', publication_year=2000, author=self.author)
        self.client = APIClient()

    def test_book_list_public(self):
        url = reverse('book-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue(len(resp.data) >= 1)

    def test_book_detail_public(self):
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['title'], 'First Book')

    def test_create_book_requires_auth(self):
        url = reverse('book_all-list')  # viewset list/create route name by router convention
        data = {'title': 'New Book', 'publication_year': 2020, 'author': self.author.pk}
        # unauthenticated should be 401 or 403 depending on config
        resp = self.client.post(url, data, format='json')
        self.assertIn(resp.status_code, (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN))

        # authenticate and retry
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        resp2 = self.client.post(url, data, format='json')
        self.assertEqual(resp2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(resp2.data['title'], 'New Book')

    def test_search_and_filter(self):
        url = reverse('book-list') + '?search=First'
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue(any('First Book' in (b.get('title') or '') for b in resp.data))