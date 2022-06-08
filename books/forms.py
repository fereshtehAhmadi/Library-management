from django import forms
from books.models import Book, Categorie, Author, Publishers

class NewBook(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(Categorie.objects.all())
    author = forms.ModelMultipleChoiceField(Author.objects.all())
    publishers = forms.ModelChoiceField(Publishers.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Book
        fields = "__all__"
        
        widgets = {
        'name' : forms.TextInput(attrs={'class': 'form-control'}),
        'discription' : forms.TextInput(attrs={'class': 'form-control'}),
        'category' : forms.TextInput(attrs={'class': 'form-control'}),
        'translator' : forms.TextInput(attrs={'class': 'form-control'}),
        'author' : forms.TextInput(attrs={'class': 'form-control'}),
       }
    