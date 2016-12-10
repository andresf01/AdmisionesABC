# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

from applications.empleados.models import *
from applications.admisiones.models import *

# Create your views here.


@login_required
def dashboard(request):
    if hasattr(request.user, 'empleado') or request.user.is_staff:
        data = {
            'empleados': len(Empleado.objects.all()),
            'periodo': Periodo.objects.get(activo=True),
            'programas': len(Programa.objects.all())
        }
        return render(request, 'administrador/dashboard.html', data)
    else:
        return redirect('home')
