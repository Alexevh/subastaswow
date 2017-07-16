# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 19:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('minimo', models.FloatField()),
                ('maximo', models.FloatField()),
                ('promedio', models.FloatField()),
                ('cantidad', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('nombre', models.CharField(max_length=200, unique=True)),
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('umbral', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='Producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ah.Producto'),
        ),
    ]
