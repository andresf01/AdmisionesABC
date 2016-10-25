from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Empleado(User):
    
    CARGO_CHOICES = (
        ('DIRECTOR', 'DIRECTOR'),
        ('OPERADOR', 'OPERADOR'),
    )
    
    documento = models.CharField(max_length=64, verbose_name='Numero de Documento')
    tipo_documento = models.CharField()
    nombre = models.CharField(max_length=64)
    cargo = models.CharField(max_length=64, choices=CARGO_CHOICES)
    cargo = models.CharField(max_length=64, choices=CARGO_CHOICES)
    direccion = models.CharField(max_length=64)
    telefono = models.CharField(max_length=64)
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido