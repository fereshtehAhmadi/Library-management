from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.models import User
from books.models import Book, BookMarck, Comment, Like
from django.contrib import messages
from extra.models import Categorie


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
    content = {
        'detail' : Book.objects.get(id=pk),
        # 'comment': Comment.objects.get(book=pk),
    }
    return render(request, 'books/detail.html', content)
    


def new_book(request):
    if request.method == 'POST':
        pass
    
