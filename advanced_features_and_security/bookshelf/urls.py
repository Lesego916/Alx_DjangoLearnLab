from django.urls import path
from . import views

urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("form/", views.form_view, name="form_view"),
    path("edit/<int:book_id>/", views.edit_book, name="edit_book"),
]
