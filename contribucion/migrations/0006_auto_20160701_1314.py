# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-07-01 18:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contribucion', '0005_auto_20160701_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contribucion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contribucion.Autor')),
                ('trabajo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contribucion.Trabajo')),
            ],
        ),
        migrations.RemoveField(
            model_name='trabajo_autor',
            name='autores',
        ),
        migrations.RemoveField(
            model_name='trabajo_autor',
            name='trabajos',
        ),
        migrations.DeleteModel(
            name='Trabajo_Autor',
        ),
        migrations.AddField(
            model_name='trabajo',
            name='participantes',
            field=models.ManyToManyField(through='contribucion.Contribucion', to='contribucion.Autor'),
        ),
    ]