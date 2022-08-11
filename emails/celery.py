from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'emails.settings')

app = Celery('emails', )

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task
def test_mail(text):
    return f'hello {text}'
