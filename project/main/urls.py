from django.urls import path

from .views import (index, detail, books_by_category, save_comment, update_comment,
                    delete_comment, create_book)

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', books_by_category, name='books_by_category'),
    path('book/<int:book_id>/', detail, name='detail'),
    path('book/add/', create_book, name='add_book'),

    path('add/comment/<int:book_id>/', save_comment, name='save_comment'),
    path('update/comment/<int:comment_id>/', update_comment, name='update_comment'),
    path('delete/comment/<int:comment_id>/', delete_comment, name='delete_comment'),
]
