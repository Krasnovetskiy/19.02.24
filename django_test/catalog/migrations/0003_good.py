# Generated by Django 4.2.10 on 2024-02-19 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_category_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Товари')),
                ('description', models.TextField(verbose_name='Description')),
                ('price', models.FloatField(verbose_name='Цена')),
            ],
        ),
    ]
