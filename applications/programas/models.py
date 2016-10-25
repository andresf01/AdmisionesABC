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
    
    codigo = models.CharField(max_length=8, unique=True)
    nombre = models.CharField(max_length=64)
    snies = models.CharField(max_length=8, verbose_name='Registro SNIES')
    creditos = models.IntegerField()
    formacion = models.CharField(max_length=64, choices=FORMACION_CHOICES)
    tipo = models.CharField(max_length=64, choices=TIPO_CHOICES)
    metodologia = models.CharField(max_length=64, choices=METODOLOGIA_CHOICES)
    titulo = models.CharField(max_length=64)
    image_url = models.CharField(max_length=256)
    
    def __str__(self):
        return self.codigo + ' - ' + self.nombre