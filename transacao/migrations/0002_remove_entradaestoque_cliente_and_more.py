# Generated by Django 5.0.6 on 2024-05-22 15:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_remove_cliente_endereco2'),
        ('estoque', '0004_delete_cliente'),
        ('servico', '0007_ordemservico_valor_custo'),
        ('transacao', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entradaestoque',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='entradaestoque',
            name='os',
        ),
        migrations.CreateModel(
            name='SaidaEstoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('criado_em', models.DateField(auto_now_add=True)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cliente.cliente')),
                ('os', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='servico.ordemservico')),
                ('produto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='estoque.product')),
            ],
        ),
    ]
