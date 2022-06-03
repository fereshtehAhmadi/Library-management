from django.contrib import admin
from books.models import Book, BookMarck, Comment, Like, LikeComment


admin.site.register(Book)
admin.site.register(BookMarck)
admin.site.register(Comment)
admin.site.register(LikeComment)
admin.site.register(Like)
