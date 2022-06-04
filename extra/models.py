from django.db import models
from accounts.models import CustomUserModel
from books.models import Book

    
        
class BookMarck(models.Model):
    book = models.ManyToManyField(Book)
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    

class Comment(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='comment')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comment')
    title = models.CharField(max_length=100)
    content = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class LikeComment(models.Model):
    comment = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUserModel, null=True, blank=True, on_delete=models.CASCADE)
    like = models.BooleanField(default=True)


class LikeBook(models.Model):
    vote_status = (
        ('L', 'Like'),
        ('D', 'Dislike'),
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='like')
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='like')
    vote = models.CharField(max_length = 1, choices = vote_status)
