# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

from applications.empleados.models import *

# Create your views here.


@login_required
def dashboard(request):
    try:
        empleado = Empleado.objects.get(documento=request.user.empleado.documento)
    except Exception:
        messages.warning(request, "El empleado no existe.")
        return redirect('home')
    return render(request, 'administrador/dashboard.html', {'empleado': empleado})
