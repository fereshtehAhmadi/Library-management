from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib import messages
from django.db.models import Count

from django.contrib.auth.decorators import login_required
from accounts.decorators import unauthenticated_user, super_user, staff_user

from django.contrib.auth.models import User
from accounts.models import CustomUserModel
from books.models import Book, Categorie, Author, Publishers, BookRequest
from extra.models import Comment, LikeBook, LikeComment, BookMarck
from loan.models import LoanModel, DebtModel


@login_required(login_url='login')
def add_loan(request, pk):
        book = Book.objects.get(id=pk)
    # try:
        user = CustomUserModel.objects.get(user=request.user)
        start = LoanModel.objects.filter(user=user, status='S')
        to_be_returned = LoanModel.objects.filter(user=user, status='T')
        loan = start | to_be_returned
        valid = loan.count()
        if valid < 5:
            debt = DebtModel.objects.filter(user=user)
            if debt.exists():
                l = []
                for obj in debt:
                    l.append(int(obj.amount))
                listsum = sum(l)
        
                if listsum > 0:
                    messages.error(request, 'Please pay your fines first.')
                else:
                    loan = LoanModel.objects.create(user=user,book=book, status='S')
                    messages.success(request, 'Your request has been successfully submitted...')
            else:
                loan = LoanModel.objects.create(user=user,book=book, status='S')
                messages.success(request, 'Your request has been successfully submitted...')
        else:
            messages.error(request, 'You can only borrow 5 books from the library at the same time!!')
    # except:
    #     messages.error(request, 'Please complete your user information!!')
        return redirect('detail', pk=book.id)


@login_required(login_url='login')
def loan_list(request):
    try:
        user = CustomUserModel.objects.get(user=request.user)
        start = LoanModel.objects.filter(user=user, status='S')
        to_be_returned = LoanModel.objects.filter(user=user, status='T')
        loan = start | to_be_returned
        content = {
            'loan': loan,
        }
    except:
        messages.error(request, 'Please complete your user information!!')
    return render(request, 'loan/loan_list.html', content)


@login_required(login_url='login')
def done_payment(request):
    custom_user = CustomUserModel.objects.get(user=request.user)
    debt = DebtModel.objects.filter(user=custom_user)
    if debt.exists():
        for obj in debt:
            obj.amount = 0
            obj.save()
        return redirect('loan')
    else:
        return redirect('loan')



@login_required(login_url='login')
def payment(request):
    return render(request, 'loan/payment.html')



    



@login_required(login_url='login')
@staff_user
def check_receive(request):
    if request.method == 'POST':
        id = request.POST['id']
        book = Book.objects.get(id=id)
        return redirect('user_loan', pk=book.id)
    return render(request, 'loan/receive.html')


@login_required(login_url='login')
@staff_user
def user_loan(request, pk):
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
    return render(request, 'loan/user_loan.html', content)


def receive(request, pk):
    book = Book.objects.get(id=pk)
    loan = LoanModel.objects.get(book=pk)
    loan.status = 'R'
    loan.save()
    return redirect('check_receive')
