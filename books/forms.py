from django import forms
from books.models import Book, Categorie, Author, Publishers
from accounts.models import CustomUserModel


class NewBook(forms.ModelForm):    
    hidden_user = forms.CharField(widget=forms.HiddenInput())
    category = forms.ModelMultipleChoiceField(Categorie.objects.all(), required=True)
    author = forms.ModelMultipleChoiceField(Author.objects.all(), required=True)
    publishers = forms.ModelChoiceField(Publishers.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    translator = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Book
        exclude = ("user",)
        
        widgets = {
        'name' : forms.TextInput(attrs={'class': 'form-control'}),
        'discription' : forms.TextInput(attrs={'class': 'form-control'}),
        'category' : forms.TextInput(attrs={'class': 'form-control'}),
        'author' : forms.TextInput(attrs={'class': 'form-control'},),
       }


class EditBook(forms.ModelForm):    
    hidden_user = forms.CharField(widget=forms.HiddenInput())
    
    class Meta:
        model = Book
        exclude = ("user",)
