from django.contrib import admin
from django.urls import path, include
from books import views

urlpatterns = [
    path('', views.books, name="home"),
    path('detail/<int:pk>', views.detail_book, name="detail"),
    path('like/<int:pk>', views.like_books, name="like"),
    path('dislike/<int:pk>', views.dislike_books, name="dislike"),
    path('category/<int:cats>', views.category, name="category"),
    path('author/<int:auth>', views.search_author, name="author"),
    path('comment/<int:pk>', views.comment, name="comment"),
    path('acceptable/<int:pk>/<int:bk>', views.like_comment, name="acceptable"),
    path('new_book/', views.new_book, name="new_book"),
    path('delete_comment/<int:pk>', views.delete_comment, name="delete_comment"),
    ]
