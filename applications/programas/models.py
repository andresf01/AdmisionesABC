# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Programa(models.Model):
    
    FORMACION_CHOICES = (
        ('PROFESIONAL', 'PROFESIONAL'),
        ('TECNOLOGICA', 'TECNOLOGICA'),
        ('TECNICA', 'TECNICA'),
    )
    
    TIPO_CHOICES = (
        ('PREGRADO', 'PREGRADO'),
        ('POSGRADO', 'POSGRADO'),
    )
    
    METODOLOGIA_CHOICES = (
        ('PRESENCIAL', 'PRESENCIAL'),
        ('SEMI-PRESENCIAL', 'SEMI-PRESENCIAL'),
        ('A DISTANCIA', 'A DISTANCIA'),
    )
    
    codigo = models.CharField(max_length=8, unique=True, verbose_name='Código')
    nombre = models.CharField(max_length=64)
    snies = models.CharField(max_length=8, verbose_name='Registro SNIES')
    creditos = models.IntegerField(verbose_name='Créditos')
    formacion = models.CharField(max_length=64, choices=FORMACION_CHOICES, verbose_name='Formación')
    tipo = models.CharField(max_length=64, choices=TIPO_CHOICES)
    metodologia = models.CharField(max_length=64, choices=METODOLOGIA_CHOICES, verbose_name='Metodología')
    titulo = models.CharField(max_length=64, verbose_name='Título')
    descripcion = models.CharField(max_length=512, verbose_name='Descripción')
    image_url = models.CharField(max_length=256, verbose_name='URL Imagen')
    
    def __unicode__(self):
        return self.codigo + ' - ' + self.nombre