from django.contrib import admin
from django.urls import path, include
from books import views

urlpatterns = [
    path('books/', views.books, name="books"),
    ]