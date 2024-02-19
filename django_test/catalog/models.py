from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField('Name', max_length=15, unique=True)
    description = RichTextField('Description')

    def __str__(self):
        return self.name


class Good(models.Model):
    name = models.CharField('Товари', max_length=20)
    description = models.TextField('Description')
    price = models.FloatField('Цена')
    active = models.BooleanField('Active', default=False, help_text='отобразить товар на сайте')

    def __str__(self):
        return f'{self.name} - {self.price}'
