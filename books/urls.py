from django.contrib import admin
from django.urls import path, include
from books import views

urlpatterns = [
    path('', views.books, name="home"),
    path('search/', views.search, name="search"),
    path('advance_search/', views.advance_search, name='advance_search'),
    path('category/<int:cats>', views.category, name="category"),
    path('author/<int:auth>', views.search_author, name="author"),
    
    path('detail/<int:pk>', views.detail_book, name="detail"),
    path('book_info/<int:pk>', views.book_info, name="book_info"),
    path('edit_book/<int:pk>', views.edit_book, name="edit_book"),
    
    path('new_book/', views.new_book, name="new_book"),
    path('new_author/', views.new_author, name="new_author"),
    path('new_publisher/', views.new_publisher, name="new_publisher"),
    path('new_category/', views.new_catrgory, name="new_category"),
    
    path('request_book/', views.request_book, name="request_book"),
    path('request_list/', views.request_list, name="request_list"),
    path('request_done/<int:pk>', views.request_book_done, name="request_done"),
    

    ]
