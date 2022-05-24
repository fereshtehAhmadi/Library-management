from django.db import models
from django.contrib.auth.models import User
from extra.models import Author, Categorie, Publishers


class Book(models.Model):
    name = models.CharField(max_length=100)
    cover = models.ImageField(null=True, blank=True)
    description = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    translator = models.CharField(max_length=100)
    condition = models.BooleanField(default=True)   #active
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ManyToManyField(Author)
    category = models.ManyToManyField(Categorie)
    publishers = models.ManyToManyField(Publishers)
        
    def __str__(self):
        return self.book_name


class BookMarck(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    like = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    

class Like(models.Model):
    Vote_status = (
        ('L', 'Like'),
        ('D', 'Dislike'),
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length = 1, choices = Vote_status)

