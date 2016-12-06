from __future__ import unicode_literals

from django.db import models

from applications.admisiones.models import *

# Create your models here.


class Pago(models.Model):
    aspirante = models.OneToOneField(Aspirante)
    pagado = models.BooleanField(default=False)
