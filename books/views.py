from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.models import User
from books.models import Book, BookMarck, Comment, Like
from django.contrib import messages
from extra.models import Categorie
from django.db.models import Count


def books(request):
    context = {
        'books': Book.objects.all(),
        'cate': Categorie.objects.all(),
    }
    return render(request, 'index.html', context)


def category(request, cats):
    context = {
        'book': get_list_or_404(Book, category= cats),
        'cate': Categorie.objects.all(),
    }
    return render(request, 'index.html', context)



def detail_book(request, pk):
    book = Book.objects.get(id=pk)
    content = {
        'detail' : book,
        'comment': Comment.objects.filter(book=pk),
        'like' : Like.objects.filter(book=book, vote='L').count(),
        'dislike' : Like.objects.filter(book=book, vote='D').count(),
    }
    return render(request, 'books/detail.html', content)
    


def new_book(request):
    if request.method == 'POST':
        pass
    
