# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ah', '0002_auto_20170126_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]
