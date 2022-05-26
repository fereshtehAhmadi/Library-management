from extra.models import Author, Categorie, Publishers
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
import random


class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of extra to be created')
        parser.add_argument('-a', '--extra', action='store_true', help='Create a extra')

    def handle(self, *args, **kwargs):
        total = kwargs['total']

        
        for i in range(total):
            
            category = get_random_string()
            author = get_random_string()
            discription = get_random_string()
            publishers = get_random_string()


            Categorie.objects.create(category=category)
            Author.objects.create(name=author, description= discription)
            Publishers.objects.create(name=publishers)


# python manage.py create_extra 5