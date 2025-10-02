from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path("book/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
]

urlpatterns += [
    path("login/", LoginView.as_view(template_name="login"),
    path("logout/", LogoutView.as_view(template_name="logout"),
    path("register/", views.register, name="register"),
]

urlpatterns += [
    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),
]

urlpatterns += [
    path("add_book/", views.add_book, name="add_book"),
    path("edit_book/", views.edit_book, name="edit_book"),
    path("delete-book/", views.delete_book, name="delete_book"),
]
