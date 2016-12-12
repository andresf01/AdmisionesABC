# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import F, Count, Func, DateField
from django.db.models.functions import Cast

from applications.empleados.models import *
from applications.admisiones.models import *

# Create your views here.


@login_required
def dashboard(request):
    if hasattr(request.user, 'empleado') or request.user.is_staff:
        periodo = None
        parejas = []
        try:
            periodo = Periodo.objects.get(activo=True)
            parejas = Aspirante.objects.filter(programa__periodo__id=periodo.id).annotate(fecha=Cast(F('date_joined'), DateField())).values('fecha').annotate(inscritos=Count('fecha'))
            # print parejas
            if not parejas:
                messages.warning(request, 'No hay aspirantes en el periodo seleccionado.')
        except Exception as ex:
            print ex.message
        data = {
            'empleados': Empleado.objects.all().count(),
            'periodo': periodo,
            'programas': Programa.objects.all().count(),
            'parejas': parejas
        }
        return render(request, 'administrador/dashboard.html', data)
    else:
        return redirect('home')
