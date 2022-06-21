from django.contrib import admin
from django.urls import path, include
from loan import views

urlpatterns = [
    path('', include('books.urls')),
    path('add_loan/<int:pk>', views.add_loan, name="add_loan"),
    path('loan/', views.loan_list, name="loan"),
    path('payment/', views.payment, name="payment"),
    path('done_payment/', views.done_payment, name="done_payment"),
    path('check_receive/', views.check_receive, name="check_receive"),
    path('user_loan/<int:pk>', views.user_loan, name="user_loan"),
    path('receive/<int:pk>', views.receive, name="receive"),
    ]