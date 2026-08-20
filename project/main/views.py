from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest

from .models import Category, Book, Comment
from .forms import CommentForm, BookForm


# ----------------------start book-----------------------------

def index(request):
    books = Book.objects.filter(published=True)
    categories = Category.objects.all()
    context = {
        'books': books,
        'categories': categories
    }
    return render(request, 'main/index.html', context)


def books_by_category(request, category_id):
    categories = Category.objects.all()
    books = Book.objects.filter(category_id=category_id, published=True)
    context = {
        "books": books,
        "categories": categories
    }
    return render(request, "main/index.html", context)


def detail(request: HttpRequest, book_id):
    book = get_object_or_404(Book, pk=book_id, published=True)
    comments = Comment.objects.filter(book_id=book_id).order_by('-created')
    context = {"book": book, "comments": comments}
    return render(request, "main/detail.html", context)


def create_book(request):
    if request.user.is_staff:
        if request.method == "POST":
            form = BookForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                book = form.save()
                return redirect("detail", book_id=book.id)
        else:
            form = BookForm()
        context = {
            "form": form
        }
        return render(request, "main/add_book.html", context)
    else:
        return redirect("home")




# ----------------------end book-----------------------------


# ----------------------start comment-----------------------------


def save_comment(request: HttpRequest, book_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # text = request.POST.get('text')
            form = CommentForm(data=request.POST)
            if form.is_valid():
                book = get_object_or_404(Book, pk=book_id, published=True)
                comment = Comment.objects.create(text=form.cleaned_data.get("text"), book=book, user=request.user)
            else:
                print("simvollar soni 500 tadan ko'p")
            return redirect('detail', book_id=book_id)
        else:
            return redirect('home')
    else:
        print('login qiling')
        return redirect('home')


def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user.is_authenticated and request.user == comment.user:
        if request.method == 'POST':
            form = CommentForm(data=request.POST)
            if form.is_valid():
                comment.text = form.cleaned_data.get("text")
                comment.save()
                return redirect("detail", book_id=comment.book.id)
        else:
            form = CommentForm(initial={"text": comment.text})
        context = {
            "form": form
        }
        return render(request, "main/comment_update.html", context)
    else:
        print('login qiling')
        return redirect('home')


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user.is_authenticated and request.user == comment.user or request.user.is_superuser:
        book_id = comment.book.id
        if request.method == 'POST':
            comment.delete()
            return redirect('detail', book_id=book_id)
        else:
            return render(request, "main/confirm_delete.html", {"comment": comment})
    else:
        print('login qiling')
        return redirect('home')

# ----------------------end comment-----------------------------
