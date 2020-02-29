from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from .models import Book


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {"books": books})


def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'book_detail.html', {"book": book, "pk": pk})


@require_http_methods(["GET", "POST"])
def book_new(request):
    pass


def book_edit(request, pk):
    pass


def book_delete(request):
    pass
