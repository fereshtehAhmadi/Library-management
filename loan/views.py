from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from books.models import Book, Categorie, Author, Publishers, BookRequest
from extra.models import Comment, LikeBook, LikeComment, BookMarck
from loan.models import LoanModel, DebtModel
from django.contrib import messages
from django.db.models import Count
from accounts.models import CustomUserModel


def add_loan(request, pk):
    try:
        user = CustomUserModel.objects.get(user=request.user)
        book = Book.objects.get(id=pk)
        valid = LoanModel.objects.filter(user=user, status='S').count()
        if valid < 5:
            loan = LoanModel.objects.create(user=user,book=book, status='S')
            messages.success(request, 'Your request has been successfully submitted...')
        else:
            messages.error(request, 'You can only borrow 5 books from the library at the same time!!')
    except:
        messages.error(request, 'Please complete your user information!!')
    return redirect('detail', pk=book.id)


def loan_lis(request):
    try:
        user = CustomUserModel.objects.get(user=request.user)
        content = {
            'loan': LoanModel.objects.filter(user=user, status='S'),
        }
    except:
        messages.error(request, 'Please complete your user information!!')
    return render(request, 'loan/loan_list.html', content)
        
