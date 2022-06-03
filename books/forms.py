from django import forms
from books.models import Book
from extra.models import Categorie, Author, Publishers


class NewBook(forms.ModelForm):
    category = forms.ModelChoiceField(Categorie.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    author = forms.ModelChoiceField(Author.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
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
    
    
# class NewBook(forms.ModelForm):
#     name = forms.CharField(label='book name', widget=forms.TextInput(attrs={'class': 'form-control'}))    
        
#     class Meta:
#         model = Book
#         fields = ('name', 'author', 'translator', 'publishers', 'cover', 'discription', 'category')
        
#         widgets = {
#         'name' : forms.TextInput(attrs={'class': 'form-control'}),
#         'author' : forms.TextInput(attrs={'class': 'form-control' ,}),
#         'translator' : forms.TextInput(attrs={'class': 'form-control'}),
#         'publishers' : forms.TextInput(attrs={'class': 'form-control'}),
#         'cover' : forms.TextInput(attrs={'class': 'form-control'}),
#         'discription' : forms.TextInput(attrs={'class': 'form-control'}),
#         'category' : forms.TextInput(attrs={'class': 'form-control'}),
#        }