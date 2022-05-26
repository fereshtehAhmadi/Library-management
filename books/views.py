from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from books.models import Book, BookMarck, Comment, Like
from django.contrib import messages


def books(request):
    book = Book.objects.get()
    return render(request, 'books/books.html')


def new_book(request):
    if request.method == 'POST':
        pass
    
