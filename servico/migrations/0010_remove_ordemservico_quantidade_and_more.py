# Generated by Django 5.0.6 on 2024-05-23 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0009_ordemservico_valor_produto_alter_ordemservico_valor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordemservico',
            name='quantidade',
        ),
        migrations.RemoveField(
            model_name='ordemservico',
            name='valor_produto',
        ),
    ]
