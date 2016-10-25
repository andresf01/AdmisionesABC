from __future__ import unicode_literals

from django.db import models

# Create your models here.

# class Persona(models.Model):
#     id = models.CharField(max_length=32, primary_key=True)
#     nombre = models.CharField(max_length=64)
#     apellido = models.CharField(max_length=64)
    
    
class Resultado():
    snp = models.CharField(max_length=32, primary_key=True)
    lectura = models.IntegerField()
    matematicas = models.IntegerField()
    naturales = models.IntegerField()
    sociales = models.IntegerField()
    ingles = models.IntegerField()