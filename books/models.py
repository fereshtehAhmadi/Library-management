from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustomUserModel



class Categorie(models.Model):
    category = models.CharField(max_length=20)
    
    def __str__(self):
        return self.category


class Publishers(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    

class Author(models.Model):
    name = models.CharField(max_length = 20)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Authorss'
        verbose_name = 'Authorrr'
        
        
class Book(models.Model):
    name = models.CharField(max_length=100)
    cover = models.ImageField(null=True, blank=True, default='default.jpg', upload_to='images/') 
    description = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    translator = models.CharField(max_length=100)
    condition = models.BooleanField(default=True)   #active
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='books')
    author = models.ManyToManyField(Author)
    category = models.ManyToManyField(Categorie)
    publishers = models.ForeignKey(Publishers, on_delete=models.CASCADE, related_name='books')
    
    def __str__(self):
        return self.name + '        ' + str(self.id)
        
    

class BookRequest(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50, null=True, blank=True) #just say one 
    translator = models.CharField(max_length=50, null=True, blank=True)
    publisher = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.user.username} request {self.name}'
