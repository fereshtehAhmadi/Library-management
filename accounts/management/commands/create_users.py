from django.contrib.auth.models import User
from accounts.models import Profile
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

# import factory
# from faker import Faker
# from .providers import CustomPhoneProvider
#  phone_number = factory.LazyAttribute(lambda _: fake.phone_number())


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')
        parser.add_argument('-p', '--prefix', type=str, help='Define a username prefix')
        parser.add_argument('-a', '--admin', action='store_true', help='Create an admin account')
        parser.add_argument('-s', '--staff', action='store_true', help='Create an staff account')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        prefix = kwargs['prefix']
        admin = kwargs['admin']
        staff = kwargs['staff']

        for i in range(total):
            
            
            if prefix:
                username = '{prefix}_{random_string}'.format(prefix=prefix, random_string=get_random_string())
            else:
                username = get_random_string()

            if admin:
                User.objects.create_superuser(username=username, email=f'{username}@gmail.com', password='123')
            elif staff:
                User.objects.create_user(username=username, email=f'{username}@gmail.com', password='123', is_staff=True)
            else:
                User.objects.create_user(username=username, email=f'{username}@gmail.com', password='123')
                
                
# python manage.py create_users 2 -a
# python manage.py create_users 2 -s
# python manage.py create_users 2