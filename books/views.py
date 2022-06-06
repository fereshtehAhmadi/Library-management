from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from books.models import Book, Categorie, Author, Publishers, BookRequest
from extra.models import Comment, LikeBook, LikeComment, BookMarck
from loan.models import LoanModel, DebtModel
from django.contrib import messages
from django.db.models import Count
from books.forms import NewBook
from accounts.models import CustomUserModel


def books(request):
    context = {
        'books': Book.objects.all(),
        'cate': Categorie.objects.all(),
    }
    return render(request, 'home.html', context)


def category(request, cats):
    context = {
        'separation': get_list_or_404(Book, category= cats),
        'cate': Categorie.objects.all(),
    }
    return render(request, 'home.html', context)


def search_author(request, auth):
    context = {
        'separation': get_list_or_404(Book, author= auth),
        'cate': Categorie.objects.all(),
    }
    return render(request, 'home.html', context)



def detail_book(request, pk):
    book = Book.objects.get(id=pk)
    content = {
        'detail' : book,
        'comment': Comment.objects.filter(book=pk),
        'like' : LikeBook.objects.filter(book=book, vote='L').count(),
        'dislike' : LikeBook.objects.filter(book=book, vote='D').count(),
        'loan': LoanModel.objects.filter(book=book, status='S').exists(),
    }
    return render(request, 'books/detail.html', content)    


# inam try except mikhad...     
@login_required(login_url='login')       
def new_book(request):
    if request.method == 'POST':
        book_form = NewBook(request.POST)
        customuser = CustomUserModel.objects.get(user=request.user)
        if book_form.is_valid():
            book_form.save(commit=False)
            book_form.user = customuser
            book_form.save_m2m()
            messages.success(request, 'Your registration was successfully done.')
            return redirect('home')
        else:
            print('this is a test in case of failure.')
    book_form = NewBook()
    content = {
        'new_book':book_form,
    }
    return render(request, 'books/add/new_books.html', content)


@login_required(login_url='login')
def new_author(request):
    if request.method == 'POST':
        pass
        
    
    
@login_required(login_url='login')
def request_book(request):
    try:
        if request.method == 'POST':
            user = CustomUserModel.objects.get(user=request.user)
            name= request.POST['name']
            author= request.POST['author']
            translator= request.POST['translator']
            publisher= request.POST['publisher']
            BookRequest.objects.create(name=name, author=author, translator=translator, publisher=publisher, user=user)
            messages.success(request, 'Your request was send successfully!')
            return redirect('request_book')
    except:
        messages.error(request, 'Please complete your user information!!')
    return render(request, 'books/request_book.html')



@login_required(login_url='login')
def request_list(request):
    content = {
        'list': BookRequest.objects.all(),
    }
    return render(request, 'other/request_list.html', content)
    