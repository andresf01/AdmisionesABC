from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group, Permission
from django.db.models import F, Count, Func, DateField
# from django.db.models import Cast
import datetime

from applications.admisiones.models import *
from forms import *

# Create your views here.


@login_required
def inscritos_por_periodo(request):
    parejas = []
    periodos = Periodo.objects.all().order_by('identificador')
    for periodo in periodos:
        # cantidad = 0
        # for oferta in periodo.oferta_set.all():
        #     cantidad += len(oferta.aspirante_set.all())
        aspirantes_periodo = Aspirante.objects.filter(programa__periodo__identificador=periodo.identificador)
        cantidad = len(aspirantes_periodo)
        pareja = (periodo, cantidad)
        parejas.append(pareja)
    data = {
        'parejas': parejas,
    }
    
    return render(request, 'reportes/inscritos_por_periodo.html', data)
    

@login_required  
def inscritos_por_oferta(request):
    parejas = []
    form = InscritosPorOfertaForm()
    if request.method == 'POST':
        form = InscritosPorOfertaForm(request.POST)
        if form.is_valid():
            periodo = form.cleaned_data['periodo']
            for oferta in periodo.oferta_set.all():
                cantidad = len(oferta.aspirante_set.all())
                pareja = (oferta, cantidad)
                parejas.append(pareja)
    data = {
        'form': form,
        'parejas': parejas,
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
            query = Aspirante.objects.filter(programa__periodo__id=periodo.id).annotate(date=Func(F('date_joined'), 'tiki')).values('date').annotate(inscritos=Count('date'))
            print query
    data = {
        'form': form,
        'parejas': parejas,
    }
    
    return render(request, 'reportes/inscritos_por_fecha_por_periodo.html', data)
