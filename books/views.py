from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Count, Q

# from urllib import quote_plus

from django.contrib.auth.decorators import login_required
from accounts.decorators import unauthenticated_user, super_user, staff_user
from django.contrib.postgres.search import SearchVector

from django.contrib.auth.models import User
from django.http import HttpResponse

from accounts.models import CustomUserModel
from books.models import Book, Categorie, Author, Publishers, BookRequest
from extra.models import Comment, LikeBook, LikeComment, BookMarck
from loan.models import LoanModel, DebtModel

from books.forms import NewBook, EditBook

# home page 
def books(request):
    p = Paginator(Book.objects.filter(condition=True).order_by('?'), 12)
    page = request.GET.get('page')
    book_list = p.get_page(page)
    context = {
        'books': book_list,
        'cate': Categorie.objects.all(),
    }
    return render(request, 'home.html', context)


def search(request):
    if request.method == 'GET':
        q = request.GET.get('q')
        if q:
           query_set = Book.objects.filter(Q(name__icontains=q) | Q(
            author__name__icontains=q) | Q(
                category__category__icontains=q), condition=True).distinct()

        if not query_set:
            return redirect('home')

        elif query_set:
            paginator = Paginator(query_set, 12)
            page = request.GET.get('page')
            book_search = paginator.get_page(page)
            
            context = {
                'page': page,
                'book_search': book_search,
                'query': str(q),
                'cate': Categorie.objects.all(),
            }
            return render(request, 'home.html', context)
    return redirect('home')




def advance_search(request):
    if request.method == 'GET':
        n = request.GET.get('n')
        a = request.GET.get('a')
        t = request.GET.get('t')
        p = request.GET.get('p')
        
        if n or a or t or p:
            query_set = Book.objects.filter(
                name__icontains=n).filter(
                author__name__icontains=a).filter(
                    translator__icontains=t).filter(
                        publishers__name__icontains=p
                    ).distinct()
            if query_set.count() > 0 :
                paginator = Paginator(query_set, 12)
                page = request.GET.get('page')
                book_search = paginator.get_page(page)
            
                context = {
                    'page': page,
                    'book_search': book_search,
                }
                return render(request, 'home.html', context)
            
            else:
                messages.error(request, 'not found!!!')
                return redirect('advance_search')
            
        
    return render(request, 'books/advance_search.html')
        


def category(request, cats):
    book = Book.objects.filter(category= cats, condition=True).count()
    if book > 0 :
        p = Paginator(Book.objects.filter(category= cats, condition=True), 12)
        page = request.GET.get('page')
        cate = p.get_page(page)
        context = {
            'separation': cate,
            'cate': Categorie.objects.all(),
        }
        return render(request, 'home.html', context)
    else:
        messages.error(request, 'not found !!!')
        return redirect('home')
        
    page = request.GET.get('page')
    cate = p.get_page(page)
    context = {
        'separation': cate,
        'cate': Categorie.objects.all(),
    }
    return render(request, 'home.html', context)


def search_author(request, auth):
    p = Paginator(get_list_or_404(Book, author= auth, condition=True), 12)
    page = request.GET.get('page')
    author = p.get_page(page)
    context = {
        'separation': author,
        'cate': Categorie.objects.all(),
    }
    return render(request, 'home.html', context)


# book detail 
def detail_book(request, pk):
    try:
        book = Book.objects.get(id=pk)
        comment = Comment.objects.filter(book=pk)
        bookmarck_status = BookMarck.objects.filter(user=request.user, book=book).exists()
        like_b = LikeBook.objects.filter(user=request.user, book=book).exists()
        LB = None
        if like_b:
            LB = LikeBook.objects.filter(user=request.user, book=book, vote='L').exists()
            
    except:
        LB = None
        bookmarck_status = False
    
    finally:   
        content = {
        'detail' : book,
        'comment': comment,
        'user': CustomUserModel.objects.get(user=request.user),
        'bookmarck_status': bookmarck_status,
        'like' : LikeBook.objects.filter(book=book, vote='L').count(),
        'color_like_b':LB,
        'dislike' : LikeBook.objects.filter(book=book, vote='D').count(),
        'loan': LoanModel.objects.filter(book=book, status='S').exists(),
        }
        return render(request, 'books/detail.html', content)  
    
    
    
@login_required(login_url='login')
@staff_user
def book_info(request, pk):
    book = Book.objects.get(id=pk)
    loan = LoanModel.objects.filter(book=book, status='S').exists()
    if loan:
        obj =LoanModel.objects.get(book=book)
        borrower = obj.user
        custom_user = CustomUserModel.objects.get(user=borrower)
        content = {
        'book': book,
        'borrower': borrower,
        'custom_user': custom_user.user.id,
        }
    else:
         content = {
        'book': book,
        }
 
    return render(request, 'books/book_info.html', content)



@login_required(login_url='login')
@staff_user  
def edit_book(request, pk):
    book = Book.objects.get(id=pk)
    book_form = NewBook(request.POST, instance=request.user)
    if request.method == 'POST':
        if book_form.is_valid():
            cd = book_form.cleaned_data
            
            book.name=cd['name']
            book.cover=cd['cover']
            book.description=cd['description']
            book.translator=cd['translator']
            book.condition=cd['condition']
            book.publishers=cd['publishers']
            book.save()
            book.author.set(cd["author"])
            book.category.set(cd["category"])
            book.save()
            return redirect('detail', pk=book.id)
        else:
            messages.error(request, book_form.errors)
    content = {
        'edit_book':book_form,
        'book': book,
    }
    return render(request, 'books/edit_book.html', content)


@login_required(login_url='login')
@staff_user 
def book_condition(request, pk):
    book = Book.objects.get(id=pk)
    if book.condition == True:
        book.condition = False
        book.save()
        return redirect('book_info', pk=book.id)
    else:
        book.condition = True
        book.save()
        return redirect('unactive_books')


@login_required(login_url='login')
@staff_user 
def unactive_books(request):
    books = Book.objects.filter(condition=False)
    return render(request, 'books/unactive_books.html', {'books': books})


# add new book   
@login_required(login_url='login')
@staff_user
def new_book(request):
    try:
        if request.method == 'POST':
            book_form = NewBook(request.POST)
            
            if book_form.is_valid():
                cd = book_form.cleaned_data
                current_user_object = CustomUserModel.objects.get(user__username=cd['hidden_user'])        
                book_obj = Book.objects.create(
                    user= current_user_object,
                    name = cd['name'],
                    cover=cd['cover'],
                    description=cd['description'],
                    translator=cd['translator'],
                    condition=cd['condition'],
                    publishers=cd['publishers'],
                )
                book_obj.author.set(cd["author"])
                book_obj.category.set(cd["category"])
                book_obj.save()
                messages.success(request, 'Your registration was successfully done.')
                return redirect('home')
            else:
                messages.error(request, book_form.errors.as_data())
        book_form = NewBook()
        content = {
            'new_book':book_form,
        }
    except:
        messages.error(request, 'Please complete you informations!!!')

    return render(request, 'books/add/new_books.html', content)


@login_required(login_url='login')
@staff_user
def new_catrgory(request):
    try:
        if request.method == 'POST':
            category = request.POST['category']
            Categorie.objects.create(category=category)
            return redirect('new_book')
        content = {
            'category': 'category',
        }
    except:
        messages.error(request, 'Please complete you informations!!!')
        
    return render(request, 'books/add/new_forenkey.html', content)



@login_required(login_url='login')
@staff_user
def new_author(request):
    try:
        if request.method == 'POST':
            author = request.POST['author']
            description = request.POST['description']
            Author.objects.create(name=author, description=description)
            return redirect('new_book')
        content = {
            'author': 'author',
        }
    except:
        messages.error(request, 'Please complete you informations!!!')
        
    return render(request, 'books/add/new_forenkey.html', content)



@login_required(login_url='login')
@staff_user
def new_publisher(request):
    try:
        if request.method == 'POST':
            publisher = request.POST['publisher']
            Publishers.objects.create(name=publisher)
            return redirect('new_book')
        content = {
            'publisher': 'publisher',
        }
    except:
        messages.error(request, 'Please complete you informations!!!')
    return render(request, 'books/add/new_forenkey.html', content)

    

# book request 
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
@staff_user
def request_list(request):
    content = {
        'list': BookRequest.objects.all(),
    }
    return render(request, 'books/request_list.html', content)


@login_required(login_url='login')
@staff_user
def request_book_done(request, pk):
    obj = BookRequest.objects.get(id=pk)
    obj.delete()
    return redirect('request_list')

