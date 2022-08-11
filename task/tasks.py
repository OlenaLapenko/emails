from celery import shared_task
from django.core.mail import send_mail


@shared_task
def mails(text, email):
    send_mail('Reminder', text, 'admin@gmail.com', [email, ], fail_silently=False)
