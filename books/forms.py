from django import forms
from books.models import Book, Categorie, Author, Publishers
from accounts.models import CustomUserModel


class BookForm(forms.ModelForm):    
    hidden_user = forms.CharField(widget=forms.HiddenInput())
    
    class Meta:
        model = Book
        exclude = ("user",)
