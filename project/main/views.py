from django.db.models import Model
from django.shortcuts import render
from django.http import Http404

from .models import Category, Book


def index(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    context = {
        'books': books,
        'categories': categories
    }
    return render(request, 'main/index.html', context)


def detail(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {"book": book}
    return render(request, "main/detail.html", context)








