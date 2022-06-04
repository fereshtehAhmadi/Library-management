from django.contrib import admin
from django.urls import path, include
from books import views

urlpatterns = [
    path('', views.books, name="home"),
    path('detail/<int:pk>', views.detail_book, name="detail"),
    path('category/<int:cats>', views.category, name="category"),
    path('author/<int:auth>', views.search_author, name="author"),
    path('new_book/', views.new_book, name="new_book"),
    path('request_book/', views.request_book, name="request_book"),
    ]
