from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import unauthenticated_user, super_user, staff_user

from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Count

from extra.models import LikeBook, Comment, BookMarck, LikeComment
from books.models import Book
from accounts.models import CustomUserModel



@login_required(login_url='login')
def add_book_marck(request, pk):
    try:
        book = Book.objects.get(id=pk)
        bookmarck = BookMarck.objects.filter(user=request.user).exists()
        validbook = BookMarck.objects.filter(user=request.user, book=book).exists()
        if not bookmarck:
            obj = BookMarck.objects.create(user=user)
            obj.book.add(book)
            obj.save()
        else:
            obj = BookMarck.objects.get(user=request.user)
            if validbook:
                obj.book.remove(book)
                obj.save()
            else:
                obj.book.add(book)
                obj.save()
    except:
        book = Book.objects.get(id=pk)
        messages.error(request, 'Please complete your user information!!')
    return redirect('detail', pk=book.id)


def book_marck(request):
    content = {
        'bookmarck': BookMarck.objects.filter(user=request.user),
    }
    return render(request, 'extra/book_marck.html', content)



@login_required(login_url='login')
def comment(request, pk):
    try:
        book = Book.objects.get(id=pk)
        customuser = CustomUserModel.objects.get(user=request.user)
        if request.method == 'POST':
            title = request.POST['title']
            content = request.POST['content']
            Comment.objects.create(title=title, content=content, book=book, user=customuser)
            return redirect('detail', pk=book.id)
    except:
        messages.error(request, 'Please complete your user information!!')
    return redirect('detail', pk=book.id)



def like_comment(request, pk, bk):
    book = Book.objects.get(id=bk)
    try:
        comment = Comment.objects.get(id=pk)
        validation = LikeComment.objects.filter(user=request.user, comment=comment).exists()
        if validation:
            valid = LikeComment.objects.filter(user=request.user, comment=comment, like=True).exists()
            if valid:
                accept = LikeComment.objects.get(user=request.user, comment=comment)
                accept.like = False
                accept.save()
            else:
                accept = LikeComment.objects.get(user=request.user, comment=comment)
                accept.like = True
                accept.save()
        else:
            LikeComment.objects.create(user=request.user, comment=comment, like=True)
        return redirect('detail', pk=book.id)
    except:
        messages.error(request, 'Please login first!!')
    return redirect('detail', pk=book.id)        
    


@login_required(login_url='login')
def like_books(request, pk):
    try:
        book = Book.objects.get(id=pk)
        validation = LikeBook.objects.filter(user=request.user, book=book)
        if validation.exists():
            valid = LikeBook.objects.filter(user=request.user, book=book, vote='L').exists()
            if not valid:
                like = LikeBook.objects.get(user=request.user, book=book)
                like.vote = 'L'
                like.save()
                return redirect('detail', pk=book.id)
        else:
            LikeBook.objects.create(user=request.user, book=book, vote='L')
            return redirect('detail', pk=book.id)
    except:
        messages.error(request, 'Please login first!!')
    return redirect('detail', pk=book.id)



@login_required(login_url='login')
def dislike_books(request, pk):
    try:
        book = Book.objects.get(id=pk)
        validation = LikeBook.objects.filter(user=request.user, book=book)
        if validation.exists():
            valid = LikeBook.objects.filter(user=request.user, book=book, vote='D').exists()
            if not valid:
                like = LikeBook.objects.get(user=request.user, book=book)
                like.vote = 'D'
                like.save()
                return redirect('detail', pk=book.id)
        else:
            LikeBook.objects.create(user=request.user, book=book, vote='D')
            return redirect('detail', pk=book.id)
    except:
        messages.error(request, 'Please login first!!')
    return redirect('detail', pk=book.id)


        
    
@login_required(login_url='login')
@staff_user 
def delete_comment(request, pk):
    obj = get_object_or_404(Comment, id=pk)
    book = Book.objects.get(comment=obj)
    obj.delete()
    return redirect('detail', pk=book.id)
        
        
