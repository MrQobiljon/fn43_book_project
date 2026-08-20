from django import forms

from .models import Book

class CommentForm(forms.Form):
    text = forms.CharField(max_length=500, label="Matni", widget=forms.Textarea(attrs={
        "style": "font-size: 22pt; padding: 15px; border-radius: 15px;",
        "rows": "4",
        "cols": "40"
    }))


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        # fields = ['title', 'introduction', 'price', 'image', 'published', 'category']
        # exclude = ['price']
        widgets = {
            'title': forms.TextInput(attrs={
                "style": "padding: 10px 10px 10px 10px; font-size: 20pt; border-radius: 15px;"
            }),
            'introduction': forms.Textarea(attrs={
                "style": "padding: 10px 10px 10px 10px; font-size: 20pt; border-radius: 15px;",
                "rows": 4,
            })
        }
        labels = {
            "title": "Nomi",
            "introduction": "Kirish",
            "price": "Narxi"
        }