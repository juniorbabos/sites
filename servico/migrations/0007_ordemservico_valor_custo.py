# Generated by Django 5.0.6 on 2024-05-21 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0006_ordemservico_observacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordemservico',
            name='valor_custo',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Valor Custo'),
        ),
    ]