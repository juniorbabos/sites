# Generated by Django 5.0.6 on 2024-05-20 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='endereco2',
        ),
    ]
