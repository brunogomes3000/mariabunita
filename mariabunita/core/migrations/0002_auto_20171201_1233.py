# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sac',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perguntas', models.CharField(max_length=500, verbose_name='Perguntas')),
                ('resposta', models.CharField(max_length=4000, verbose_name='Resposta')),
            ],
            options={
                'verbose_name': 'Sac',
                'verbose_name_plural': 'Sac',
            },
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'ordering': ['-nome'], 'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
    ]