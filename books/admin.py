from django.contrib import admin
from books.models import Book, BookMarck, Comment, Like


admin.site.register(Book)
admin.site.register(BookMarck)
admin.site.register(Comment)
admin.site.register(Like)
