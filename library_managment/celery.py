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

from books.models import Author


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(),
        test(),
    )

@app.task
def test():
    return  Author.objects.create(name='veryyyyy author', description='test')


# ------------------------------------------------------------------
# from celery import Celery
# import os
# import django

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_managment.settings')
# django.setup()

# BROKER_URL = "amqp://guest:guest@localhost:5672/"

# app = Celery(
# 	'library_managment', 
# 	broker=BROKER_URL,
# )
# app.autodiscover_tasks(packages=['tasks'])

# app.config_from_object(celeryconfig)

# app.config_from_object('library_managment.settings')

# if __name__ == '__main__':
# 	app.start()

# celery -A library_managment worker -l info
# --------------------------------------------------------------------------
# from __future__ import absolute_import, unicode_literals
# from celery.task import task
# import os
# from celery import Celery
# import celery
# from celery.schedules import crontab
# import django
# import os
# from library_managment import settings as celeryconf

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_managment.settings')
# django.setup()

# BROKER_URL = "pyamqp://guest:guest@localhost/"

# app = Celery('library_managment', broker=BROKER_URL)

# app.config_from_object('library_managment.settings')


# app.autodiscover_tasks()



# CELERY_IMPORTS = (
#     'loan.tasks.expiration',
# )

# app.conf.beat_schedule = {
#     # Executes every day at  00:00.
#     'run-every-midnight': {
#         'task': 'tasks.expiration',
#         'schedule': crontab(hour=0, minute=0),
#         'args': (),
#     },
# }


# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(
#         crontab(),
#         test(),
#     )
    
# app.conf.timezone = 'Asia/Tehran'
# from books.models import Author

# @app.task
# def test():
# 	Author.objects.create(name='very_test', description='very_test')
# 	return 1
# --------------------------------------------------------------------

