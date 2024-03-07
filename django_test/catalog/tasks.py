from celery import shared_task
from django_test.celery import app as celery_app
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)

@celery_app.task(name="send_massage")
def emailing():
    send_mail(
        'Test subject',
        '<br>Body</br>',
        'valera3001vampir@gmail.com',
        ['valera3001vampir@gmail.com'],
        fail_silently=False
    )
    logger.info('email send')
    logger.warning('email send')
    logger.critical('email send')