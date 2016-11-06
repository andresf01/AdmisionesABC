# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.decorators import login_required, user_passes_test

from models import *
from forms import *

# Create your views here.

@login_required
def crear_empleado(request):
    form = CrearEmpleadoForm()
    if request.method == 'POST':
        form = CrearEmpleadoForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 == password2:
                empleado = form.save(commit=False)
                empleado.set_password(password1)
                empleado.save()
                messages.success(request, "El empleado fue registrado con exito.")
                if empleado.cargo == 'DIRECTOR':
                    grupo = Group.objects.get(name='Director')
                elif empleado.cargo == 'OPERADOR':
                    grupo = Group.objects.get(name='Operador')
                grupo.user_set.add(empleado)
                return render(request, 'empleados/crear_empleado.html', {'form': CrearEmpleadoForm(), 'user': request.user.empleado, 'editar': False})
            messages.error(request, "Error al registrar el empleado.")
        
    return render(request, 'empleados/crear_empleado.html', {'form': form, 'user': request.user.empleado, 'editar': False})
    
    
@login_required
def editar_empleado(request, empleado_id):
    try:
        empleado = Empleado.objects.get(documento=empleado_id)
    except Exception:
        return redirect('listar_empleados')

    # instance e initial para cargar datos en los campos
    form = EditarEmpleadoForm(instance=empleado, initial=empleado.__dict__)
    if request.method == 'POST':
        form = EditarEmpleadoForm(request.POST, instance=empleado, initial=empleado.__dict__)
        if form.is_valid():
            empleado = form.save(commit=False)
            empleado.save()
            messages.success(request, "Empleado modificado correctamente.")
            return redirect('listar_empleados')
        messages.error(request, "Error al modificar el empleado.")

    return render(request, 'empleados/crear_empleado.html', {'form': form, 'user': request.user.empleado, 'editar': True})
    
    
@login_required
def ver_empleado(request, empleado_id):
    try:
        empleado = Empleado.objects.get(documento=empleado_id)
    except Exception:
        messages.warning(request, "El empleado no existe.")
        return redirect('listar_empleados')

    return render(request, 'empleados/ver_empleado.html', {'empleado': empleado})
    

@login_required
def listar_empleados(request):
    empleados = Empleado.objects.all().exclude(username=request.user.username)
    return render(request, 'empleados/listar_empleados.html', {'empleados': empleados, 'user': request.user.empleado})
    
    
@login_required
def setpassword_empleado(request, empleado_id):
    try:
        empleado = Empleado.objects.get(documento=empleado_id)
    except Exception:
        return redirect('listar_empleados')

    form = SetPasswordEmpleadoForm(empleado)
    if request.method == 'POST':
        # importante aqui siempre mandar el POST al form
        form = SetPasswordEmpleadoForm(empleado, request.POST)
        if form.is_valid():
            empleado.save()
            messages.success(request, "Contraseña cambiada satisfactoriamente.")
            return redirect('listar_empleados')

    return render(request, 'empleados/setpassword_empleado.html', {'form': form,  'user': request.user.empleado})
