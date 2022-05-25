from books.models import Book


class NewBook(forms.ModelForm):
        
    class Meta:
        model: Book
        fields: (name, cover, discription, translator, )