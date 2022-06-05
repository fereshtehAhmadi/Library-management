from django.contrib import admin
from django.urls import path, include
from extra import views

urlpatterns = [
    path('', include('loan.urls')),
    path('like/<int:pk>', views.like_books, name="like"),
    path('dislike/<int:pk>', views.dislike_books, name="dislike"),
    path('comment/<int:pk>', views.comment, name="comment"),
    path('acceptable/<int:pk>/<int:bk>', views.like_comment, name="acceptable"),
    path('delete_comment/<int:pk>', views.delete_comment, name="delete_comment"),
    path('add_book_marck/<int:pk>', views.add_book_marck, name="add_book_marck"),
    path('book_marck/', views.book_marck, name="book_marck"),
    ]
