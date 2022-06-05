from django.contrib import admin
from django.urls import path, include
from loan import views

urlpatterns = [
    path('', include('books.urls')),
    path('add_loan/<int:pk>', views.add_loan, name="add_loan"),
    path('loan/', views.loan_lis, name="loan"),
    ]