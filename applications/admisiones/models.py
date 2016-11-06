# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from applications.programas.models import *

# Create your models here.


class Periodo(models.Model):
    identificador = models.CharField(max_length=6, unique=True)
    nombre = models.CharField(max_length=64, unique=True)
    puntaje_minimo = models.IntegerField(verbose_name='Puntaje Mínimo')
    programas = models.ManyToManyField(Programa, through='Oferta')
    
    def __unicode__(self):
        return self.nombre

    
class Calendario(models.Model):
    nombre = models.CharField(max_length=64)
    descripcion = models.CharField(max_length=512)
    periodo = models.OneToOneField(Periodo)
    
    def __unicode__(self):
        return 'Calendario ' + self.periodo.periodo
    
    
class Evento(models.Model):
    titulo = models.CharField(max_length=64)
    descripcion = models.CharField(max_length=512)
    calendario = models.ForeignKey(Calendario, on_delete=models.CASCADE)
    

class Oferta(models.Model):
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE)
    cupo = models.IntegerField()
    peso_lectura = models.IntegerField(verbose_name='Peso Lectura Critica')
    peso_matematicas = models.IntegerField(verbose_name='Peso Matematicas')
    peso_naturales = models.IntegerField(verbose_name='Peso Ciencias Naturales')
    peso_sociales = models.IntegerField(verbose_name='Peso Ciencias Sociales')
    peso_ingles = models.IntegerField(verbose_name='Peso Ingles')
    peso_prueba = models.IntegerField(verbose_name='Peso Prueba Específica')
    
    def __unicode__(self):
        return self.programa.codigo + ' - ' + self.programa.nombre
    

class Aspirante(User):
    TIPO_ID_CHOICES = (
        ('CC', 'Cédula de Ciudadania'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjeria'),
    )
    
    documento = models.CharField(max_length=64, verbose_name='Número de Documento')
    tipo_documento = models.CharField(max_length=64, choices=TIPO_ID_CHOICES, verbose_name='Tipo de Documento')
    snp = models.CharField(max_length=64, verbose_name='Icfes SNP')
    puntaje_global = models.IntegerField(verbose_name='Puntaje Global')
    colegio = models.CharField(max_length=64)
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    direccion = models.CharField(max_length=64)
    telefono = models.CharField(max_length=64)
    programa = models.ForeignKey(Oferta, on_delete=models.CASCADE)
    
    def __unicode__(self):
        return self.nombre + ' ' + self.apellido