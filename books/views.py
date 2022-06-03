from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from books.models import Book, BookMarck, Comment, Like
from django.contrib import messages
from extra.models import Categorie, Author
from django.db.models import Count
from books.forms import NewBook
from accounts.models import CustomUserModel


def books(request):
    context = {
        'books': Book.objects.all(),
        'cate': Categorie.objects.all(),
    }
    return render(request, 'index.html', context)


def category(request, cats):
    context = {
        'separation': get_list_or_404(Book, category= cats),
        'cate': Categorie.objects.all(),
    }
    return render(request, 'index.html', context)


def search_author(request, auth):
    context = {
        'separation': get_list_or_404(Book, author= auth),
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


@login_required(login_url='login')
def comment(request, pk):
    book = Book.objects.get(id=pk)
    
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        customuser = CustomUserModel.objects.get(user=request.user)
        Comment.objects.create(title=title, content=content, book=book, user=customuser)
        return redirect('detail', pk=book.id)
    return redirect('detail', pk=book.id)


@login_required(login_url='login')
def like_books(request, pk):
    user = CustomUserModel.objects.get(user=request.user)
    book = Book.objects.get(id=pk)
    validation = Like.objects.filter(user=user, book=book)
    if validation.exists():
        valid = Like.objects.filter(user=user, book=book, vote='L').exists()
        if not valid:
            like = Like.objects.get(user=user, book=book)
            like.vote = 'L'
            like.save()
        return redirect('detail', pk=book.id)
    else:
        Like.objects.create(user=user, book=book, vote='L')
        return redirect('detail', pk=book.id)
    return redirect('detail', pk=book.id)


@login_required(login_url='login')
def dislike_books(request, pk):
    user = CustomUserModel.objects.get(user=request.user)
    book = Book.objects.get(id=pk)
    validation = Like.objects.filter(user=user, book=book)
    if validation.exists():
        valid = Like.objects.filter(user=user, book=book, vote='D').exists()
        if not valid:
            like = Like.objects.get(user=user, book=book)
            like.vote = 'D'
            like.save()
        return redirect('detail', pk=book.id)
    else:
        Like.objects.create(user=user, book=book, vote='D')
        return redirect('detail', pk=book.id)
    return redirect('detail', pk=book.id)


        
    
@login_required(login_url='login')   
def delete_comment(request, pk):
    obj = get_object_or_404(Comment, id=pk)
    book = Book.objects.get(comment=obj)
    obj.delete()
    return redirect('detail', pk=book.id)
        
        
@login_required(login_url='login')       
def new_book(request):
    if request.method == 'POST':
        book_form = NewBook(request.POST)
        if book_form.is_valid():
            book_form.save(commit=False)
            customuser = CustomUserModel.objects.get(user=request.user)
            book_form.user = customuser
            book_form.save()
            book_form.save_m2m()
            messages.success(request, 'Your registration was successfully done.')
            return redirect('home')
        else:
            print('this is a test in case of failure.')
    book_form = NewBook()
    content = {
        'new_book':book_form,
    }
    return render(request, 'index2.html', content)


@login_required(login_url='login')
def new_author(request):
    if request.method == 'POST':
        pass
        
    
