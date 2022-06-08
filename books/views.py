from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Count
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from accounts.models import CustomUserModel
from books.models import Book, Categorie, Author, Publishers, BookRequest
from extra.models import Comment, LikeBook, LikeComment, BookMarck
from loan.models import LoanModel, DebtModel

from books.forms import NewBook




def books(request):
    p = Paginator(Book.objects.all().order_by('?'), 12)
    page = request.GET.get('page')
    book_list = p.get_page(page)
    context = {
        'books': book_list,
        'cate': Categorie.objects.all(),
    }
    return render(request, 'home.html', context)

    

def search(request):
    if request.method == 'GET':
        searched = request.GET['searched']
        book = Book.objects.filter(name__contains=searched)
        if book.exists():
            return render(request, 'home.html', {'book_search':book})
        else:
            return render(request, 'home.html', {'searched': searched})
        
        

def category(request, cats):
    p = Paginator(get_list_or_404(Book, category= cats), 12)
    page = request.GET.get('page')
    cate = p.get_page(page)
    context = {
        'separation': cate,
        'cate': Categorie.objects.all(),
    }
    return render(request, 'home.html', context)


def search_author(request, auth):
    p = Paginator(get_list_or_404(Book, author= auth), 12)
    page = request.GET.get('page')
    author = p.get_page(page)
    context = {
        'separation': author,
        'cate': Categorie.objects.all(),
    }
    return render(request, 'home.html', context)



def detail_book(request, pk):
    book = Book.objects.get(id=pk)
    comment = Comment.objects.filter(book=pk)
    user = CustomUserModel.objects.get(user=request.user)
    bookmarck_status = BookMarck.objects.filter(user=user, book=book).exists()
    like_b = LikeBook.objects.filter(user=request.user, book=book).exists()
    if like_b:
        LB = LikeBook.objects.filter(user=request.user, book=book, vote='L').exists()
        if LB:
            color_like = 'green'
            color_dislike = 'black'
        else:
            color_like = 'black'
            color_dislike = 'red'
    else:
        color_like = 'black'
        color_dislike = 'black'    
    content = {
        'detail' : book,
        'comment': Comment.objects.filter(book=pk),
        'bookmarck_status': bookmarck_status,
        'like' : LikeBook.objects.filter(book=book, vote='L').count(),
        'color_like':color_like,
        'color_dislike':color_dislike,
        'dislike' : LikeBook.objects.filter(book=book, vote='D').count(),
        'loan': LoanModel.objects.filter(book=book, status='S').exists(),
        # 'likecomment': Comment.objects.select_related(LikeComment).count
    }
    return render(request, 'books/detail.html', content)    


# inam try except mikhad...     
@login_required(login_url='login')       
def new_book(request):
    if request.method == 'POST':
        book_form = NewBook(request.POST)
        customuser = CustomUserModel.objects.get(user=request.user)
        if book_form.is_valid():
            name = form.cleaned_data["name"]
            translator = form.cleaned_data["translator"]
            discription = form.cleaned_data["discription"]
            cover = form.cleaned_data["cover"]
            publishers = form.cleaned_data["publishers"]
            user = customuser
            new = Book.objects.create(name=name,
                       translator=translator,
                       discription=discription,
                       cover=cover,
                       publishers=publishers,
                       user=user)
            new.author.add(form.cleaned_data["author"])
            new.category.add(form.cleaned_data["category"])
            new.save()
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
def new_catrgory(request):
    if request.method == 'POST':
        category = request.POST['category']
        Categorie.objects.create(category=category)
        return redirect('new_book')
    content = {
        'category': 'category',
    }
    return render(request, 'books/add/new_forenkey.html', content)



@login_required(login_url='login')
def new_author(request):
    if request.method == 'POST':
        author = request.POST['author']
        description = request.POST['description']
        Author.objects.create(name=author, description=description)
        return redirect('new_book')
    content = {
        'author': 'author',
    }
    return render(request, 'books/add/new_forenkey.html', content)



@login_required(login_url='login')
def new_publisher(request):
    if request.method == 'POST':
        publisher = request.POST['publisher']
        Publishers.objects.create(name=publisher)
        return redirect('new_book')
    content = {
        'publisher': 'publisher',
    }
    return render(request, 'books/add/new_forenkey.html', content)

    
    
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
    