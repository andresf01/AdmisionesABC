# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-24 21:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admisiones', '0006_aspirante_fecha_inscripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aspirante',
            name='fecha_inscripcion',
        ),
    ]
