from django.db import models
from django.contrib.auth.models import User
from extra.models import Author, Categorie, Publishers


class Book(models.Model):
    name = models.CharField(max_length=100)
    cover = models.ImageField(null=True, blank=True, default='uploads/default.jpg', upload_to='images/') 
    description = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    translator = models.CharField(max_length=100)
    condition = models.BooleanField(default=True)   #active
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    author = models.ManyToManyField(Author)
    category = models.ManyToManyField(Categorie)
    publishers = models.ForeignKey(Publishers, on_delete=models.CASCADE, related_name='publisers')
        
    def __str__(self):
        return self.name


class BookMarck(models.Model):
    book = models.ManyToManyField(Book)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comment')
    title = models.CharField(max_length=100)
    content = models.TextField()
    like = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    

class Like(models.Model):
    vote_status = (
        ('L', 'Like'),
        ('D', 'Dislike'),
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='like')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like')
    vote = models.CharField(max_length = 1, choices = vote_status)



# python manage.py populate_db