# Generated by Django 4.0.6 on 2022-07-17 19:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11, null=True)),
                ('cnpj', models.CharField(max_length=14, null=True)),
                ('telefone', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=45)),
                ('endereco', models.CharField(max_length=100)),
                ('tipo', models.CharField(choices=[('PF', 'fisica'), ('PJ', 'juridica')], default='PF', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conta_origem', models.CharField(max_length=8)),
                ('conta_destino', models.CharField(max_length=8)),
                ('data_transacao', models.DateField(default=datetime.date.today)),
                ('valor', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banco', models.CharField(default='0001', max_length=4)),
                ('agencia', models.CharField(max_length=4)),
                ('conta', models.CharField(max_length=8, unique=True)),
                ('data_abertura', models.DateField(default=datetime.date.today)),
                ('deposito_inicial', models.FloatField(default=0.0, null=True)),
                ('saldo_conta', models.FloatField(default=0.0, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco_digital.cliente')),
            ],
        ),
    ]