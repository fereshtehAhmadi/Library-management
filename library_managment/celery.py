from __future__ import absolute_import, unicode_literals
from celery import task
import os
from celery import Celery
import celery
from celery.schedules import crontab
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_managment.settings')
django.setup()

BROKER_URL = "amqp://guest:guest@localhost/"

app = Celery('library_managment', broker=BROKER_URL)

app.config_from_object('django.conf:settings', namespace='CELERY')

# app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'add-every-3-seconds': {
#         'task': 'library_managment.test',
#         'schedule': 3.0,
#     },
# }

from random import choice
from string import ascii_letters
from books.models import Author

def get_random_char():
    return choice(list(ascii_letters))


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(6.0, test(get_random_char()), name='add every 10')


@app.task
def test(arg):
    obj = Author.objects.create(name='author' + arg, description='test')
    return arg 
