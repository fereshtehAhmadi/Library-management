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



def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        book = Book.objects.filter(name=searched)
        if book.exists():
            return render(request, 'home.html', {'book_search':book})
        else:
            return render(request, 'home.html', {'searched': searched})



def books(request):
    context = {
        'books': Book.objects.all()[:36],
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
    # count = 0
    # l = []
    # for obj in comment:
    #     comment = Comment.objects.get(id=obj.id)
    #     comment.title = []
    #     for i in comment.likecomment.all():
    #         if i.like == True:
    #             count += 1
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
    