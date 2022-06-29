# from __future__ import absolute_import, unicode_literals
# from celery import shared_task

# from django.conf import settings

# settings.configure()



# import django
# django.setup()

# from loan.models import LoanModel, DebtModel
# from django.contrib.auth.models import User
# from accounts.models import CustomUserModel

# @shared_task()
# def expiration():
    # loan = LoanModel.objects.all()
    # for obj in loan:
    #     diff = datetime.now() - obj.start_date
    #     if diff.days >= 30:
    #         obj.status = 'T'
    #         obj.save()
    #         expiration = diff.days - 30
    #         return diff_time(expiration, obj.id)
    # return None


# def diff_time(expiration, pk):
    # loan = LoanModel.objects.get(id=pk)
    # a = int(expiration) / 7           
    # return debt(a=a, book=loan.book)


# def debt(a, book):
    # debt = DebtModel.objects.get(book=book)
    # debt.amount = a * 2000
    # debt.save()
    # return debt.amount
