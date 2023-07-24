from django import forms

from books.models import Book, Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'author', 'genre']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname']
