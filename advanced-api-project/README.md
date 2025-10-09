# advanced-api-project

Django + Django REST Framework project with:

- Author and Book models
- BookSerializer (with validation)
- AuthorSerializer (nested books)
- Generic views + ViewSet for CRUD
- Filtering / Searching / Ordering
- Token authentication

## Quick notes

1. Install requirements:
   pip install -r requirements.txt

2. Run migrations:
   python manage.py migrate

3. Create a superuser:
   python manage.py createsuperuser

4. Run server:
   python manage.py runserver

5. Token obtain endpoint:
   POST /api-token-auth/ with { "username": "...", "password": "..." }
