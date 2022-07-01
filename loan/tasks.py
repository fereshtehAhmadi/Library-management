# from celery.utils.log import get_task_logger
# from library_managment.celery import app
# from books.models import Author


# logger = get_task_logger(__name__)


# @app.task
# def add_author():
# 	Author.objects.create(name='very_test', description='very_test')
# 	return 1

# ---------------------------------------------------------
# @app.task
# def expiration():
#     loan = LoanModel.objects.all()
#     for obj in loan:
#         if obj.status == 'S':
#             diff = datetime.now() - obj.start_date
#             if diff.days >= 30:
#                 obj.status = 'T'
#                 obj.save()
#                 expiration = diff.days - 30
                
#                 a = int(expiration) / 7
                
#                 debt = DebtModel.objects.create(loan=obj.id, book=obj.book, user=obj.user, amount=a*2000)
                
#         elif obj.status == 'T':
#             diff = datetime.now() - obj.start_date
#             if diff.days >= 30:
#                 expiration = diff.days - 30
#                 a = int(expiration) / 7
#                 debt = DebtModel.objects.get(loan=obj.id)
#                 debt.amount = a * 2000
#                 debt.save()
#     return 'done!!'




# -------------------------------------------------------------
# from __future__ import absolute_import, unicode_literals
# from celery import shared_task
# import celery
# import os
# import django
# from library_managment.celery import app

# @app.task
# def test():
#     return 'test'

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_managment.settings')
# django.setup()

# from django.conf import settings
# settings.configure()

# from loan.models import LoanModel, DebtModel
# from django.contrib.auth.models import User
# from accounts.models import CustomUserModel

# from datetime import datetime


# @shared_task()
# def expiration():
#     loan = LoanModel.objects.all()
#     for obj in loan:
#         if obj.status == 'S':
#             obj.status = 'T'
#             obj.save()
#     return None

# ----------------------------------
# @celery.task
# def expiration():
#     loan = LoanModel.objects.all()
#     for obj in loan:
#         if obj.status == 'S' or obj.status == 'T':
#             diff = datetime.now() - obj.start_date
#             if diff.days >= 30:
#                 obj.status = 'T'
#                 obj.save()
#                 expiration = diff.days - 30
                
#                 a = int(expiration) / 7
                
#                 debt = DebtModel.objects.get(book=obj.book, user=obj.user)
#                 debt.amount = a * 2000
#                 debt.save()
#     return 'done!!'

# -------------------------------------------------
# def diff_time(expiration, pk):
#     loan = LoanModel.objects.get(id=pk)
#     a = int(expiration) / 7           
#     return debt(a=a, book=loan.book)


# def debt(a, book):
#     debt = DebtModel.objects.get(book=book)
#     debt.amount = a * 2000
#     debt.save()
#     return debt.amount
