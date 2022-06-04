from django.contrib import admin
from books.models import Book, Author, Categorie, Publishers, BookRequest


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Categorie)
admin.site.register(Publishers)
admin.site.register(BookRequest)
