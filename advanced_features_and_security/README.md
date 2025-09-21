# Advanced Features and Security (advanced_features_and_security)

This folder contains the Django project required for the "Advanced Features and Security" tasks.

Key files added:
- Custom user model: `bookshelf/models.py` (CustomUser, CustomUserManager)
- Admin registration: `bookshelf/admin.py`
- Permissions on Book model (can_view, can_create, can_edit, can_delete)
- Security settings in `LibraryProject/settings.py`:
  - AUTH_USER_MODEL = "bookshelf.CustomUser"
  - SECURE_SSL_REDIRECT = True
  - SECURE_HSTS_SECONDS = 31536000
  - SESSION_COOKIE_SECURE = True
  - CSRF_COOKIE_SECURE = True
  - SECURE_CONTENT_TYPE_NOSNIFF = True
  - X_FRAME_OPTIONS = "DENY"

Notes:
- Templates that use CSRF token: `templates/bookshelf/form_example.html`
- Views that enforce permissions use `permission_required` decorator.
- Adjust `SECRET_KEY` and other settings for production as required.
