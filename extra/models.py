from django.db import models
from django.contrib.auth.models import User


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
        verbose_name_plural = 'Authors'
        verbose_name = 'Author'