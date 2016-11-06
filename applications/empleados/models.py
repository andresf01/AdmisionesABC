# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Empleado(User):
    
    TIPO_DOCUMENTO_CHOICES = (
        ('CC', 'Cedula de Ciudadania'),
        ('CE', 'Cedula de Extranjeria'),
    )
    
    CARGO_CHOICES = (
        ('DIRECTOR', 'DIRECTOR'),
        ('OPERADOR', 'OPERADOR'),
    )
    
    documento = models.CharField(max_length=64, unique=True, verbose_name='Numero de Documento')
    tipo_documento = models.CharField(max_length=64, choices=TIPO_DOCUMENTO_CHOICES,verbose_name='Tipo de Documento')
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    cargo = models.CharField(max_length=64, choices=CARGO_CHOICES)
    direccion = models.CharField(max_length=64)
    telefono = models.CharField(max_length=64)
    
    def __unicode__(self):
        return self.nombre + ' ' + self.apellido