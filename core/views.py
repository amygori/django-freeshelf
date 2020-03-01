from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from .models import Book, Category
from .forms import BookForm


def book_list(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    return render(request, 'book_list.html',
                  {"books": books, "categories": categories})


def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    category = book.category
    return render(request, 'book_detail.html',
                  {"book": book, "category": category, "pk": pk})


@require_http_methods(['GET', 'POST'])
def book_new(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'forms/book_form.html', {'form': form})


@require_http_methods(['GET', 'POST'])
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)

    return render(request, 'forms/book_form.html', {'form': form})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')


def books_by_category(request, slug):
    category = Category.objects.get(slug=slug)
    books_by_category = Book.objects.filter(category=category)
    return render(request, 'books_by_category.html', {'books': books_by_category, 'category': category})
