from django.shortcuts import render
from django.http import Http404


books = [
    {"id": 1, "title": "Yashil chiroq", "price": 8.55, "author": "Alksandr Grin"},
    {"id": 2, "title": "Tirilish", "price": 10.2, "author": "Lev Tolstory"},
    {"id": 3, "title": "Raqamli Qal'a", "price": 10.5, "author": "Den Broun"},
    {"id": 4, "title": "Alkimyogar", "price": 9.77, "author": "Paolo"},
    {"id": 5, "title": "Sariq devni minib", "price": 8.90, "author": "Hudoyberdi To'xtaboyev"},
    {"id": 6, "title": "Yevirilish", "price": 11.8, "author": "Kafka"},
]


def index(request):
    return render(request, 'main/index.html', {'books': books})


def detail(request, book_id):
    for book in books:
        if book.get('id') == book_id:
            return render(request, "main/detail.html", {"book": book})
    raise Http404("Book Not Found")








