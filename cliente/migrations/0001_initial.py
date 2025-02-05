# Generated by Django 5.0.6 on 2024-05-20 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('telefone', models.CharField(max_length=100, verbose_name='Telefone')),
                ('cpf', models.CharField(max_length=100, null=True)),
                ('endereco', models.CharField(max_length=200, verbose_name='Endereço')),
                ('data_criada', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('endereco2', models.CharField(max_length=200, verbose_name='Endereço')),
            ],
        ),
    ]
