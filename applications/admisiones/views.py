# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group, Permission

from forms import *
from models import *

# Create your views here.


def inscripcion(request):
    form = CrearAspiranteForm()
    if request.method == 'POST':
        form = CrearAspiranteForm(request.POST, request=request)
        if form.is_valid():
            aspirante = form.save(commit=False)
            username = form.cleaned_data['documento']
            password = form.cleaned_data['snp']
            aspirante.username = username
            aspirante.set_password(password)
            aspirante.save()
            grupo = Group.objects.get(name='Aspirante')
            grupo.user_set.add(aspirante)
            return redirect('admisiones')
        
    return render(request, 'admisiones/inscripcion.html', {'form':form})


def info(request):
    return render(request, 'admisiones/info.html')

@login_required
def editar_aspirante(request, aspirante_id):
    try:
        aspirante = Aspirante.objects.get(documento=aspirante_id)
    except:
        return redirect('listar_aspirantes')
    form = EditarAspiranteForm(instance=aspirante, initial=aspirante.__dict__)
    data = {
        'form': form,
        'user': request.user.empleado,
    }
    if request.method == 'POST':
        form = EditarAspiranteForm(request.POST, instance=aspirante, initial=aspirante.__dict__)
        if form.is_valid():
            aspirante = form.save(commit=False)
            username = form.cleaned_data['documento']
            password = form.cleaned_data['snp']
            aspirante.username = username
            aspirante.set_password(password)
            aspirante.save()
            # aspirante = form.save()
            messages.success(request, 'Aspirante modificado correctamente.')
            data['form'] = form = EditarAspiranteForm(instance=aspirante, initial=aspirante.__dict__)
            return render(request, 'admisiones/editar_aspirante.html', data)
        messages.error(request, 'Error al modificar el periodo.')
        data['form'] = form
        
    return render(request, 'admisiones/editar_aspirante.html', data)
    
   
@login_required
def dashboard(request):
    try:
        aspirante = Aspirante.objects.get(documento=request.user.aspirante.documento)
    except:
        messages.warning(request, "El aspirante no existe.")
        return redirect('home')
    return render(request, 'admisiones/dashboard.html', {'aspirante': aspirante})
    

@login_required
def crear_periodo(request):
    form = CrearPeriodoForm()
    if request.method == 'POST':
        form = CrearPeriodoForm(request.POST)
        if form.is_valid():
            periodo = form.save()
            messages.success(request, "El periodo fue registrado con exito.")
            return render(request, 'admisiones/crear_periodo.html', {'form': CrearPeriodoForm(), 'user': request.user.empleado, 'editar':False})
        messages.error(request, "Error al registrar el periodo.")
        
    return render(request, 'admisiones/crear_periodo.html', {'form': form, 'user': request.user.empleado, 'editar': False})
    
    
@login_required
def editar_periodo(request, periodo_id):
    try:
        periodo = Periodo.objects.get(nombre=periodo_id)
    except Exception:
        return redirect('listar_periodos')

    # instance e initial para cargar datos en los campos
    form = EditarPeriodoForm(instance=periodo, initial=periodo.__dict__)
    if request.method == 'POST':
        form = EditarPeriodoForm(request.POST, instance=periodo, initial=periodo.__dict__)
        if form.is_valid():
            periodo = form.save()
            messages.success(request, "Periodo modificado correctamente.")
            return redirect('listar_periodos')
        messages.error(request, "Error al modificar el periodo.")

    return render(request, 'admisiones/crear_periodo.html', {'form': form, 'user': request.user.empleado, 'editar': True})
    

@login_required
def listar_periodos(request):
    periodos = Periodo.objects.all()
    return render(request, 'admisiones/listar_periodos.html', {'periodos': periodos})
    

@login_required
def listar_calendarios(request):
    calendarios = Calendario.objects.all()
    return render(request, 'admisiones/listar_calendarios.html', {'calendarios': calendarios})
    
    
@login_required
def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'admisiones/listar_eventos.html', {'eventos': eventos})
    
    
@login_required
def listar_aspirantes(request):
    aspirantes = Aspirante.objects.all()
    return render(request, 'admisiones/listar_aspirantes.html', {'aspirantes': aspirantes, 'periodo': 'TODOS LOS PERIODOS'})
    
@login_required
def listar_aspirantes_periodo(request, periodo_id):
    aspirantes = []
    try:
        periodo = Periodo.objects.get(nombre=periodo_id)
        oferta = periodo.oferta_set.all()
        for o in oferta:
            if o.periodo.nombre == periodo.nombre:
                aspirantes += o.aspirante_set.all()
    except Exception as ex:
        print ex.message
        return redirect('listar_periodos')
    print aspirantes
    return render(request, 'admisiones/listar_aspirantes.html', {'aspirantes': aspirantes, 'periodo': periodo_id})
    

@login_required
def crear_oferta(request):
    form = CrearOfertaForm()
    if request.method == 'POST':
        form = CrearOfertaForm(request.POST)
        if form.is_valid():
            oferta = form.save()
            messages.success(request, "La oferta fue registrada con exito.")
            return render(request, 'admisiones/crear_oferta.html', {'form': CrearOfertaForm(), 'user': request.user.empleado, 'editar':False})
        messages.error(request, "Error al registrar la oferta.")
        
    return render(request, 'admisiones/crear_oferta.html', {'form': form, 'user': request.user.empleado, 'editar': False})
    
    
@login_required
def editar_oferta(request, oferta_id):
    try:
        oferta = Oferta.objects.get(id=oferta_id)
    except Exception:
        return redirect('listar_periodos')

    # instance e initial para cargar datos en los campos
    form = EditarOfertaForm(instance=oferta, initial=oferta.__dict__)
    if request.method == 'POST':
        form = EditarOfertaForm(request.POST, instance=oferta, initial=oferta.__dict__)
        if form.is_valid():
            oferta = form.save()
            messages.success(request, "oferta modificada correctamente.")
            return redirect('listar_oferta_periodo', periodo_id=oferta.periodo.nombre)
        messages.error(request, "Error al modificar la oferta.")

    return render(request, 'admisiones/crear_oferta.html', {'form': form, 'user': request.user.empleado, 'editar': True})
    

@login_required
def listar_oferta_periodo(request, periodo_id):
    try:
        periodo = Periodo.objects.get(nombre=periodo_id)
        oferta = periodo.oferta_set.all()
    except Exception as ex:
        print ex.message
        return redirect('listar_periodos')
    return render(request, 'admisiones/listar_oferta.html', {'oferta': oferta, 'periodo': periodo_id})