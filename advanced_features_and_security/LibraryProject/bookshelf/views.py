from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book
from .forms import ExampleForm

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    return render(request, 'bookshelf/form_example.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, book_id):
    return render(request, 'bookshelf/form_example.html')

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, book_id):
    return render(request, 'bookshelf/form_example.html')

def example_form_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            return render(request, 'bookshelf/form_example.html', {'form': form, 'success': True})
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

