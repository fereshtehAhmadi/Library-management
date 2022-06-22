from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from loan.tasks import expiration


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')


app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()



@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
       


app.conf.beat_schedule = {
    'add-every-day': {
        'task': 'tasks.expiration',
        'schedule': crontab(minute=0, hour=0),
    },
}