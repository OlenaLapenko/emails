from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_mail(text, email):
    send_mail('Reminder', text, 'admin@gmail.com', [email,], fail_silently=False,)