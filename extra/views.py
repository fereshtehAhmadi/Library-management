from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from extra.models import LikeBook, Comment, BookMarck, LikeComment
from books.models import Book
from django.contrib import messages
from django.db.models import Count
from accounts.models import CustomUserModel



@login_required(login_url='login')
def add_book_marck(request, pk):
    book = Book.objects.get(id=pk)
    user = CustomUserModel.objects.get(user=request.user)
    bookmarck = BookMarck.objects.filter(user=user).exists()
    if not bookmarck:
        obj = BookMarck.objects.create(user=user)
        obj.book.add(book)
        obj.save()
    else:
        obj = BookMarck.objects.get(user=user)
        obj.book.add(book)
        obj.save()
    return redirect('detail', pk=book.id)


def book_marck(request):
    user = CustomUserModel.objects.get(user=request.user)
    bookmarck = BookMarck.objects.filter(user=user)
    content = {
        'book': get_list_or_404(Book, id= bookmarck.book),
    }
    return render(request, 'extra/book_marck.html', content)



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



def like_comment(request, pk, bk):
    book = Book.objects.get(comment=bk)
    user = CustomUserModel.objects.get(user=request.user)
    comment = Comment.objects.get(id=pk)
    validation = LikeComment.objects.filter(user=user, comment=comment).exists()
    if validation:
        valid = LikeComment.objects.filter(user=user, comment=comment, like=True).exists()
        if valid:
            accept = LikeComment.objects.get(user=user, comment=comment)
            accept.like = False
            accept.save()
        else:
            accept = LikeComment.objects.get(user=user, comment=comment)
            accept.like = True
            accept.save()
    else:
        LikeComment.objects.create(user=user, comment=comment, like=True)
    return redirect('detail', pk=book.id)        
    


@login_required(login_url='login')
def like_books(request, pk):
    user = CustomUserModel.objects.get(user=request.user)
    book = Book.objects.get(id=pk)
    validation = LikeBook.objects.filter(user=user, book=book)
    if validation.exists():
        valid = LikeBook.objects.filter(user=user, book=book, vote='L').exists()
        if not valid:
            like = LikeBook.objects.get(user=user, book=book)
            like.vote = 'L'
            like.save()
            return redirect('detail', pk=book.id)
    else:
        LikeBook.objects.create(user=user, book=book, vote='L')
        return redirect('detail', pk=book.id)
    return redirect('detail', pk=book.id)


@login_required(login_url='login')
def dislike_books(request, pk):
    user = CustomUserModel.objects.get(user=request.user)
    book = Book.objects.get(id=pk)
    validation = LikeBook.objects.filter(user=user, book=book)
    if validation.exists():
        valid = LikeBook.objects.filter(user=user, book=book, vote='D').exists()
        if not valid:
            like = LikeBook.objects.get(user=user, book=book)
            like.vote = 'D'
            like.save()
            return redirect('detail', pk=book.id)
    else:
        LikeBook.objects.create(user=user, book=book, vote='D')
        return redirect('detail', pk=book.id)
    return redirect('detail', pk=book.id)


        
    
@login_required(login_url='login')   
def delete_comment(request, pk):
    obj = get_object_or_404(Comment, id=pk)
    book = Book.objects.get(comment=obj)
    obj.delete()
    return redirect('detail', pk=book.id)
        
        
