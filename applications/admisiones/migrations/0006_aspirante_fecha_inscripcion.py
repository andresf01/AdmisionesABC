# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-24 20:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admisiones', '0005_auto_20161113_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='aspirante',
            name='fecha_inscripcion',
            field=models.DateField(default=datetime.date(2016, 11, 24), verbose_name='Fecha de Inscripci\xf3n'),
        ),
    ]