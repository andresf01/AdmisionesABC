# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-27 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programa',
            name='codigo',
            field=models.CharField(max_length=8, unique=True, verbose_name='C\xf3digo'),
        ),
        migrations.AlterField(
            model_name='programa',
            name='creditos',
            field=models.IntegerField(verbose_name='Cr\xe9ditos'),
        ),
        migrations.AlterField(
            model_name='programa',
            name='descripcion',
            field=models.CharField(max_length=512, verbose_name='Descripci\xf3n'),
        ),
        migrations.AlterField(
            model_name='programa',
            name='formacion',
            field=models.CharField(choices=[('PROFESIONAL', 'PROFESIONAL'), ('TECNOLOGICA', 'TECNOLOGICA'), ('TECNICA', 'TECNICA')], max_length=64, verbose_name='Formaci\xf3n'),
        ),
        migrations.AlterField(
            model_name='programa',
            name='image_url',
            field=models.CharField(max_length=256, verbose_name='URL Imagen'),
        ),
        migrations.AlterField(
            model_name='programa',
            name='metodologia',
            field=models.CharField(choices=[('PRESENCIAL', 'PRESENCIAL'), ('SEMI-PRESENCIAL', 'SEMI-PRESENCIAL'), ('A DISTANCIA', 'A DISTANCIA')], max_length=64, verbose_name='Metodolog\xeda'),
        ),
        migrations.AlterField(
            model_name='programa',
            name='titulo',
            field=models.CharField(max_length=64, verbose_name='T\xedtulo'),
        ),
    ]
