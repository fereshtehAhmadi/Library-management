from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustomUserModel
from books.models import Book

    
        
class BookMarck(models.Model):
    book = models.ManyToManyField(Book)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.user.user.username}'
    
    
    

class Comment(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='comment')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comment')
    title = models.CharField(max_length=100)
    content = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.user.username} write comment for {self.book.id}'
    
    def like_c(comment_id):
        comment_obj = Comment.objects.get(id=comment_id)
        obj_list = comment_obj.likecomment.all()
        return obj_list.filter(like=True).count()
    # {{ obj.like_c | obj.id }}
    #  annonate
    # {{ obj.likecomment.count }}

class LikeComment(models.Model):
    comment = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.CASCADE, related_name='likecomment')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.user.username} like {self.comment.title}'


class LikeBook(models.Model):
    vote_status = (
        ('L', 'Like'),
        ('D', 'Dislike'),
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='like')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like')
    vote = models.CharField(max_length = 1, choices = vote_status)
    
    def __str__(self):
            return f'{self.user.username} like {self.book.id}'
