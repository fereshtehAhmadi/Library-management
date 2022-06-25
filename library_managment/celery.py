from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from loan.tasks import expiration


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_managment.settings')

app = Celery('library_managment')


app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()


app.conf.beat_schedule = {
    'add-every-day': {
        'task': 'tasks.expiration',
        'schedule': crontab(minute=0, hour=0),
    },
}