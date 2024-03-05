from django.core.mail import send_mail
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('send email')
        send_mail(
            'Test subject',
            '<br>Body</br>',
            'valera3001vampir@gmail.com',
            ['valera3001vampir@gmail.com'],
            fail_silently=False
        )
        print('send email')
