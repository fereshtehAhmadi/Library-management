from django.db import models
from books.models import Book
from django.contrib.auth.models import User


class Categorie(models.Model):
    category = models.CharField(max_length=20)
    
    def __str__(self):
        return self.category


class Publishers(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    like = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title