# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-13 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admisiones', '0002_auto_20161113_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='aspirante',
            name='ponderado',
            field=models.IntegerField(default=0),
        ),
    ]
