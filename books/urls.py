from django.contrib import admin
from django.urls import path, include
from books import views

urlpatterns = [
    path('', views.books, name="home"),
    path('detail/<int:pk>', views.detail_book, name="detail"),
    path('category/<int:cats>', views.category, name="category"),
    path('comment/<int:pk>', views.comment, name="comment"),
    path('delete_comment/<int:pk>', views.delete_comment, name="delete_comment"),
    ]
