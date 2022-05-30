from django.contrib import admin
from django.urls import path, include
from books import views

urlpatterns = [
    path('', views.books, name="home"),
    path('detail/<int:pk>', views.detail_book, name="detail"),
    path('category/<int:cats>', views.category, name="category"),
    ]
