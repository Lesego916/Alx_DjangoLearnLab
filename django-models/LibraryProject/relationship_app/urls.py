from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
]

urlpatterns += [
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("register/", views.register, name="register"),
]

urlpatterns += [
    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),
]

urlpatterns += [
    path("add-book/", views.add_book, name="add_book"),
    path("edit-book/", views.edit_book, name="edit_book"),
    path("delete-book/", views.delete_book, name="delete_book"),
]
