# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from applications.programas.models import *

# Create your models here.


class Periodo(models.Model):
    periodo = models.CharField(max_length=64, primary_key=True)
    puntaje_minimo = models.IntegerField(verbose_name='Puntaje Minimo')
    programas = models.ManyToManyField(Programa, through='Oferta')
    
    def __str__(self):
        return self.periodo

    
class Calendario(models.Model):
    nombre = models.CharField(max_length=64)
    descripcion = models.CharField(max_length=256)
    periodo = models.OneToOneField(Periodo)
    
    
class Evento(models.Model):
    titulo = models.CharField(max_length=64)
    descripcion = models.CharField(max_length=128)
    calendario = models.ForeignKey(Calendario, on_delete=models.CASCADE)
    

class Oferta(models.Model):
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE)
    cupo = models.IntegerField()
    peso_lectura = models.IntegerField()
    peso_matematicas = models.IntegerField()
    peso_naturales = models.IntegerField()
    peso_sociales = models.IntegerField()
    peso_ingles = models.IntegerField()
    peso_prueba = models.IntegerField()
    
    def __str__(self):
        return self.programa.codigo + ' - ' + self.programa.nombre
    

class Aspirante(User):
    TIPO_ID_CHOICES = (
        ('CC', 'Cedula de Ciudadania'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cedula de Extranjeria'),
    )
    
    documento = models.CharField(max_length=64, verbose_name='Numero de Documento')
    tipo_documento = models.CharField(max_length=64, choices=TIPO_ID_CHOICES, verbose_name='Tipo de Documento')
    snp = models.CharField(max_length=64, verbose_name='Icfes SNP')
    puntaje_global = models.IntegerField(verbose_name='Puntaje Global')
    colegio = models.CharField(max_length=64)
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    direccion = models.CharField(max_length=64)
    telefono = models.CharField(max_length=64)
    programa = models.ForeignKey(Oferta, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre + " " + self.apellido