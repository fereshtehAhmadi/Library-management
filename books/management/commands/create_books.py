from books.models import Book, BookMarck, Comment, Like
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
import random


class Command(BaseCommand):
    help = 'Create random category'
    
    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of BOOKS to be created')
        parser.add_argument('-a', '--boook', action='store_true', help='Create a BOOKS')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        boook = kwargs['boook']
        
        for i in range(total):
            
            name = get_random_string()
            discription = get_random_string()
            translator = get_random_string()
            title = get_random_string()
            content = get_random_string()
            num = random.randint(0, 300)
            vote_status = ['L', 'D']
            choice = random.choice(vote_status)
            rand = random.randint(1, 7)
            user = User.objects.filter(id=rand)
            book = Book.objects.filter(id=rand)

            if boook:
                Book.objects.create(name=name, description=discription, translator=translator, user=user)
                Comment.objects.create(title=title, content=content, like=num, user=user, book=book) #like
                Like.objects.create(vote=choice, user=user, book=book)
            else:
                Book.objects.create(name=name, description=discription, translator=translator, user=user)
                Comment.objects.create(title=title, content=content, like=num, user=user, book=book) #like
                Like.objects.create(vote=choice, user=user, book=book)


# python manage.py create_books 5