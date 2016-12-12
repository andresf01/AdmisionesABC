from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group, Permission
from django.db.models import F, Count, Func, DateField
from django.db.models.functions import Cast
import datetime

from applications.admisiones.models import *
from forms import *

# Create your views here.


@login_required
def inscritos_por_periodo(request):
    lista = []
    periodos = Periodo.objects.all().order_by('identificador')
    if not periodos:
        messages.warning(request, 'No hay periodos registrados en el sistema.')
    else:
        for periodo in periodos:
            inscritos = Aspirante.objects.filter(programa__periodo__identificador=periodo.identificador).count()
            admitidos = Aspirante.objects.filter(programa__periodo__identificador=periodo.identificador, admitido=True).count()
            programas = periodo.oferta_set.all().count()
            obj = {
                'periodo': periodo,
                'inscritos': inscritos,
                'admitidos': admitidos,
                'programas': programas
            }
            lista.append(obj)
    data = {
        'lista': lista,
    }
    
    return render(request, 'reportes/inscritos_por_periodo.html', data)
    

@login_required  
def inscritos_por_oferta(request):
    lista = []
    form = InscritosPorOfertaForm()
    if request.method == 'POST':
        form = InscritosPorOfertaForm(request.POST)
        if form.is_valid():
            periodo = form.cleaned_data['periodo']
            ofertas = periodo.oferta_set.all()
            if not ofertas:
                messages.warning(request, 'El periodo seleccionado no tiene ningun programa ofertado.')
            else:
                for oferta in periodo.oferta_set.all():
                    inscritos = oferta.aspirante_set.all().count()
                    admitidos = oferta.aspirante_set.filter(admitido=True).count()
                    obj = {
                        'oferta': oferta,
                        'inscritos': inscritos,
                        'admitidos': admitidos
                    }
                    lista.append(obj)
    data = {
        'form': form,
        'lista': lista,
    }
    
    return render(request, 'reportes/inscritos_por_oferta.html', data)
    
    
@login_required  
def inscritos_por_fecha_por_periodo(request):
    parejas = []
    form = InscritosPorFechaForm()
    if request.method == 'POST':
        form = InscritosPorFechaForm(request.POST)
        if form.is_valid():
            periodo = form.cleaned_data['periodo']
            parejas = Aspirante.objects.filter(programa__periodo__id=periodo.id).annotate(fecha=Cast(F('date_joined'), DateField())).values('fecha').annotate(inscritos=Count('fecha'))
            # print parejas
            if not parejas:
                messages.warning(request, 'No hay aspirantes en el periodo seleccionado.')
    data = {
        'form': form,
        'parejas': parejas,
    }
    
    return render(request, 'reportes/inscritos_por_fecha_por_periodo.html', data)
    
    
@login_required  
def inscritos_por_programa(request):
    lista = []
    form = InscritosPorProgramaForm()
    if request.method == 'POST':
        form = InscritosPorProgramaForm(request.POST)
        if form.is_valid():
            programa = form.cleaned_data['programa']
            ofertas = programa.oferta_set.all().order_by('periodo__identificador')
            if not ofertas:
                messages.warning(request, "El programa no ha sido ofertado en ningun periodo de admisiones.")
            else:
                for oferta in ofertas:
                    inscritos = oferta.aspirante_set.all().count()
                    admitidos = oferta.aspirante_set.filter(admitido=True).count()
                    obj = {
                        'oferta': oferta,
                        'inscritos': inscritos,
                        'admitidos': admitidos
                    }
                    lista.append(obj)
                
    data = {
        'form': form,
        'lista': lista,
    }
    
    return render(request, 'reportes/inscritos_por_programa.html', data)
