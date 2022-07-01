from __future__ import absolute_import, unicode_literals
from celery import Celery
import celery
from celery.schedules import crontab
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_managment.settings')
django.setup()

BROKER_URL = "amqp://guest:guest@localhost/"

app = Celery('library_managment', broker=BROKER_URL)

timezone='Asia/Tehran'

enable_utc=True

app.config_from_object('django.conf:settings', namespace='CELERY')


from loan.models import LoanModel, DebtModel
from datetime import datetime

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Execute daily at midnight...
    sender.add_periodic_task(
        crontab(minute=0, hour=0),
        test(),
    )

@app.task
def test():
    loan = LoanModel.objects.all()
    for obj in loan:
        if obj.status == 'S':
            diff = datetime.now().date() - obj.payment_date.date()
            if diff.days >= 30:
                obj.status = 'T'
                obj.save()
                expiration = diff.days - 30
                
                a = int(expiration) / 7
                
                debt = DebtModel.objects.create(loan=obj, book=obj.book, user=obj.user, amount=a*2000)
                
        elif obj.status == 'T':
            diff = datetime.now().date() - obj.payment_date.date()
            if diff.days >= 30:
                expiration = diff.days - 30
                a = int(expiration) / 7
                debt = DebtModel.objects.get(loan=obj)
                debt.amount = a * 2000
                debt.save()
    return 'done!!'
