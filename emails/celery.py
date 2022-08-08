from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'emails.settings')

app = Celery('emails', brocker='localhost:6379/0', backend='localhost:6379/0')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task
def test_mail(text):
    return f'hello {text}'
