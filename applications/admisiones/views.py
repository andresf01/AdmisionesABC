# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group, Permission
from django_ajax.decorators import ajax
import urllib
import urllib2
import json
import random

from admisionesabc.global_variables import *
from forms import *
from models import *
from applications.pagos.models import *

# Create your views here.
    
    
def inscripcion_exitosa(request):
    return render(request, 'success_pages/inscripcion_exitosa.html')
    
    
def inscripciones_cerradas(request):
    return render(request, 'error_pages/inscripciones_cerradas.html')
    
    
def no_admisiones(request):
    return render(request, 'error_pages/no_admisiones.html')
    
    
def no_resultados(request):
    return render(request, 'error_pages/no_resultados.html')
    

# Prueba para renders
def prueba(request):
    return render(request, 'admisiones/lista_admitidos.html')

def info(request):
    return render(request, 'admisiones/info.html')
    
    
def info_movil(request):
    return render(request, 'admisiones/info_movil.html')
    
    
def calendario(request):
    return render(request, 'admisiones/calendario.html')
    
    
def calendario_movil(request):
    return render(request, 'admisiones/calendario_movil.html')
    
    
def inscripcion(request):
    periodo = get_periodo_actual()
    if periodo:
        if not periodo.hay_resultados:
            form = CrearAspiranteForm()
            if request.method == 'POST':
                form = CrearAspiranteForm(request.POST, request=request)
                if form.is_valid():
                    aspirante = form.save(commit=False)
                    username = form.cleaned_data['documento'] + '-' + periodo.identificador
                    password = form.cleaned_data['snp']
                    aspirante.username = username
                    aspirante.set_password(password)
                    aspirante.save()
                    pago = Pago()
                    pago.aspirante = aspirante
                    pago.save()
                    grupo = Group.objects.get(name='Aspirante')
                    grupo.user_set.add(aspirante)
                    return inscripcion_exitosa(request)
        else:
            return inscripciones_cerradas(request)
    else:
        return no_admisiones(request)
        
    return render(request, 'admisiones/inscripcion.html', {'form':form})
    
    
def admitidos(request):
    parejas_oferta_admitidos = []
    periodo = None
    try:
        periodo = Periodo.objects.get(activo=True)
    except Exception as ex:
        print ex.message
        return no_admisiones(request)
    if periodo:
        if periodo.hay_resultados:
            for oferta in periodo.oferta_set.all():
                admitidos = oferta.aspirante_set.all().order_by('-ponderado')
                pareja = (oferta, admitidos)
                parejas_oferta_admitidos.append(pareja)
        else:
            return no_resultados(request)
    
    return render(request, 'admisiones/admitidos.html', {'parejas_oferta_admitidos': parejas_oferta_admitidos})
    
    
def resultados_oferta(request):
    periodo = None
    try:
        periodo = Periodo.objects.get(activo=True)
    except Exception as ex:
        print ex.message
    if periodo:
        if periodo.hay_resultados:
            pareja = None
            form = ResultadosForm()
            if request.method == 'POST':
                form = ResultadosForm(request.POST)
                if form.is_valid():
                    oferta = form.cleaned_data['programa']
                    if oferta:
                        if oferta.periodo.hay_resultados:
                            resultados = oferta.aspirante_set.all().order_by('-ponderado')
                            pareja = {}
                            pareja['oferta'] = oferta
                            pareja['resultados'] = resultados
                        else:
                            return no_resultados(request)
            return render(request, 'admisiones/admitidos.html', {'form': form, 'pareja': pareja, 'ajax':True})
        else:
            return no_resultados(request)
    else:
        return no_admisiones(request)
    
    
def resultados_oferta_movil(request):
    periodo = None
    try:
        periodo = Periodo.objects.get(activo=True)
    except Exception as ex:
        print ex.message
    if periodo:
        if periodo.hay_resultados:
            pareja = None
            form = ResultadosForm()
            if request.method == 'POST':
                form = ResultadosForm(request.POST)
                if form.is_valid():
                    oferta = form.cleaned_data['programa']
                    if oferta:
                        if oferta.periodo.hay_resultados:
                            resultados = oferta.aspirante_set.all().order_by('-ponderado')
                            pareja = {}
                            pareja['oferta'] = oferta
                            pareja['resultados'] = resultados
                        else:
                            return no_resultados(request)
            return render(request, 'admisiones/admitidos_movil.html', {'form': form, 'pareja': pareja, 'ajax':True})
        else:
            return no_resultados(request)
    else:
        return no_admisiones(request)
    

@ajax
def resultados_oferta_ajax(request):
    response = []
    if request.method == 'GET':
        oferta_id = request.GET['oferta_id']
        try:
            oferta = Oferta.objects.get(id=oferta_id)
        except Exception as ex:
            print ex.message
        if oferta:
            if oferta.periodo.hay_resultados:
                resultados = oferta.aspirante_set.all().order_by('-ponderado')
                for aspirante in resultados:
                    obj = {
                        'documento': aspirante.documento,
                        'nombre': aspirante.nombre,
                        'apellido': aspirante.apellido,
                        'ponderado': aspirante.ponderado,
                        'nota_admision': aspirante.nota_admision
                    }
                    response.append(obj)
            else:
                return no_resultados(request)
    
    return response
    
    
@login_required
def listar_resultados(request, periodo_id):
    resultados = []
    periodo = None
    try:
        periodo = Periodo.objects.get(identificador=periodo_id)
        if periodo.hay_resultados:
            resultados = Aspirante.objects.filter(programa__periodo__id=periodo.id).order_by('-ponderado', 'programa')
            print resultados
        return render(request, 'admisiones/listar_resultados.html', {'resultados': resultados, 'nombre_periodo': periodo.nombre})
    except Exception as ex:
        print ex.message
        return redirect('listar_periodos')
    
    
@login_required
def calcular_admitidos(request, periodo_id):
    nombre_periodo = 'Ninguno'
    periodo = None
    try:
        periodo = Periodo.objects.get(identificador=periodo_id)
        nombre_periodo = periodo.nombre
        ofertas = periodo.oferta_set.all()
        for oferta in ofertas:
            aspirantes = []
            aspirantes += oferta.aspirante_set.all()
            procesar_aspirantes_oferta(oferta, aspirantes)
        periodo.hay_resultados = True
        periodo.save()
        return redirect('listar_resultados', periodo_id)
    except Exception as ex:
        print ex.message
        return redirect('listar_periodos')
        
    
def procesar_aspirantes_oferta(oferta, aspirantes):
    for aspirante in aspirantes:
        if aspirante.pago.pagado == True:
            decoded_json = get_resultado(aspirante)
            if len(decoded_json) == 1:
                resultado = decoded_json[0]
                resultado_puntaje_global = resultado['lectura_critica'] + resultado['matematicas'] + resultado['sociales'] + resultado['naturales'] + resultado['ingles']
                if resultado_puntaje_global >= oferta.periodo.puntaje_minimo:
                    if aspirante.puntaje_global == resultado_puntaje_global:
                        ponderado = aspirante.programa.peso_lectura * resultado['lectura_critica']
                        ponderado += aspirante.programa.peso_matematicas * resultado['matematicas']
                        ponderado += aspirante.programa.peso_sociales * resultado['sociales']
                        ponderado += aspirante.programa.peso_naturales * resultado['naturales']
                        ponderado += aspirante.programa.peso_ingles * resultado['ingles']
                        ponderado += aspirante.programa.peso_prueba * random.randint(0, 100)
                        ponderado /= 100.0
                        aspirante.ponderado = ponderado
                        aspirante.save()
                    else:
                        aspirante.admitido = False
                        aspirante.nota_admision = 'No coincide con el registro del ICFES'
                        aspirante.save()
                else:
                    aspirante.admitido = False
                    aspirante.nota_admision = 'No cumple con el puntaje mínimo de inscripción'
                    aspirante.save()
            else:
                aspirante.admitido = False
                aspirante.nota_admision = 'No figura en la base datos del ICFES'
                aspirante.save()
        else:
            aspirante.admitido = False
            aspirante.nota_admision = 'No realizó el pago de los derechos de inscripción'
            aspirante.save()
            
    aspirantes.sort(key=lambda x: x.ponderado, reverse=True)
    cupo = oferta.cupo
    for aspirante in aspirantes:
        if cupo > 0 and aspirante.ponderado > 0:
            aspirante.admitido = True
            aspirante.nota_admision = 'Admitido primer semestre'
            aspirante.save()
            cupo -= 1
    

def get_resultado(aspirante):
    url = 'https://morning-brushlands-79611.herokuapp.com/v1/resultados/'
    values = {
        'format': 'json',
        'codigo': aspirante.snp,
    }
    
    data = urllib.urlencode(values)
    full_url = url + '?' + data
    response = urllib2.urlopen(full_url)
    the_page = response.read()
    resultado = json.loads(the_page)
    return resultado


@login_required
def editar_aspirante(request, aspirante_id):
    try:
        aspirante = Aspirante.objects.get(documento=aspirante_id)
    except:
        return redirect('listar_aspirantes')
    form = EditarAspiranteForm(instance=aspirante, initial=aspirante.__dict__)
    data = {
        'form': form,
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
    except Exception as ex:
        print ex.message
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
            return render(request, 'admisiones/crear_periodo.html', {'form': CrearPeriodoForm(), 'editar':False})
        messages.error(request, "Error al registrar el periodo.")
        
    return render(request, 'admisiones/crear_periodo.html', {'form': form, 'editar': False})
    
    
@login_required
def editar_periodo(request, periodo_id):
    try:
        periodo = Periodo.objects.get(identificador=periodo_id)
    except Exception:
        return redirect('listar_periodos')

    # instance e initial para cargar datos en los campos
    form = EditarPeriodoForm(instance=periodo, initial=periodo.__dict__)
    if request.method == 'POST':
        form = EditarPeriodoForm(request.POST, instance=periodo, initial=periodo.__dict__)
        if form.is_valid():
            periodo = form.save()
            messages.success(request, "Periodo modificado correctamente.")
            if not periodo.hay_resultados:
                aspirantes = Aspirante.objects.filter(programa__periodo__id=periodo.id)
                for aspirante in aspirantes:
                    aspirante.ponderado = 0
                    aspirante.admitido = False
                    aspirante.nota_admision = 'No admitido (cupo alcanzado)'
                    aspirante.save()
            return redirect('listar_periodos')
        messages.error(request, "Error al modificar el periodo.")

    return render(request, 'admisiones/crear_periodo.html', {'form': form, 'editar': True})
    

@login_required
def listar_periodos(request):
    periodos = Periodo.objects.all().order_by('identificador')
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
    aspirantes = Aspirante.objects.all().order_by('id')
    return render(request, 'admisiones/listar_aspirantes.html', {'aspirantes': aspirantes, 'periodo': 'TODOS LOS PERIODOS'})
    
@login_required
def listar_aspirantes_periodo(request, periodo_id):
    aspirantes = []
    try:
        periodo = Periodo.objects.get(identificador=periodo_id)
        aspirantes = Aspirante.objects.filter(programa__periodo__id=periodo.id).order_by('id')
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
            return render(request, 'admisiones/crear_oferta.html', {'form': CrearOfertaForm(), 'editar':False})
        messages.error(request, "Error al registrar la oferta.")
        
    return render(request, 'admisiones/crear_oferta.html', {'form': form, 'editar': False})
    
    
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
            return redirect('listar_oferta_periodo', periodo_id=oferta.periodo.identificador)
        messages.error(request, "Error al modificar la oferta.")

    return render(request, 'admisiones/crear_oferta.html', {'form': form, 'editar': True})
    

@login_required
def listar_oferta_periodo(request, periodo_id):
    try:
        periodo = Periodo.objects.get(identificador=periodo_id)
        oferta = periodo.oferta_set.all()
    except Exception as ex:
        print ex.message
        return redirect('listar_periodos')
    return render(request, 'admisiones/listar_oferta.html', {'oferta': oferta, 'periodo': periodo_id})
    
   
def get_periodo_actual():
    periodo = None
    try:
        periodo = Periodo.objects.get(activo=True)
    except Exception as ex:
        print ex.message
    return periodo