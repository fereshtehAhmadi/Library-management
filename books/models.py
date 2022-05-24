from django.db import models
from accounts.models import Profile
from django.contrib.auth.models import User


class Book(models.Model):
    name = models.CharField(max_length=100)
    cover = models.ImageField(null=True, blank=True)
    description = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    translator = models.CharField(max_length=100)
    condition = models.BooleanField(default=True)   #active
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # writer = models.ForeignKey('Writer',on_delete=models.CASCADE)
    # category = models.ForeignKey('Categorie',on_delete=models.CASCADE)
    # publishers = models.ForeignKey('Publishers', on_delete=models.CASCADE)
    # like = models.ForeignKey('Like', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.book_name


class BookMarck(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)