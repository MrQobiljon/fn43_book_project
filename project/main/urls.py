from django.urls import path

from .views import index, detail

urlpatterns = [
    path('', index, name='home'),
    path('book/<int:book_id>/', detail, name='detail'),
]
