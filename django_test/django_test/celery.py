import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_test.settings')
app = Celery(broker='amqp=//admin:1111@rabbit:5672', backend='rpc://')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.broker_heartbeat = 0
