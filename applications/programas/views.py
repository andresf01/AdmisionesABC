from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

from forms import *
from models import *
from admisionesabc.global_variables import *
from applications.admisiones.models import *

# Create your views here.


def programas(request):
    ofertas = Oferta.objects.filter(periodo__activo=True)
    return render(request, 'programas/programas.html', {'ofertas': ofertas})
    
    
def programas_movil(request):
    ofertas = Oferta.objects.filter(periodo__activo=True)
    return render(request, 'programas/programas_movil.html', {'ofertas': ofertas})
    
    
def programa(request, programa_id):
    try:
        oferta = Oferta.objects.get(periodo__activo=True, programa__codigo=programa_id)
    except Exception as ex:
        print ex.message
        messages.warning(request, "El programa o la oferta no existen.")
        return redirect('programas')

    return render(request, 'programas/programa.html', {'oferta': oferta})
    

@login_required
def crear_programa(request):
    form = CrearProgramaForm()
    if request.method == 'POST':
        form = CrearProgramaForm(request.POST)
        if form.is_valid():
            programa = form.save()
            return redirect('listar_programas')

    return render(request, 'programas/crear_programa.html', {'form': form, 'editar': False})
    
    
@login_required
def editar_programa(request, programa_id):
    try:
        programa = Programa.objects.get(codigo=programa_id)
    except Exception:
        return redirect('listar_programas')

    # instance e initial para cargar datos en los campos
    form = EditarProgramaForm(instance=programa, initial=programa.__dict__)
    if request.method == 'POST':
        form = EditarProgramaForm(request.POST, instance=programa, initial=programa.__dict__)
        if form.is_valid():
            programa = form.save()
            messages.success(request, "Programa modificado correctamente.")
            return redirect('listar_programas')

    return render(request, 'programas/crear_programa.html', {'form': form, 'editar': True})
    
    
@login_required
def ver_programa(request, programa_id):
    try:
        programa = Programa.objects.get(codigo=programa_id)
    except Exception:
        messages.warning(request, "El programa no existe.")
        return redirect('listar_programas')

    return render(request, 'programas/ver_programa.html', {'programa': programa})
    
    
@login_required
def listar_programas(request):
    programas = Programa.objects.all()
    return render(request, 'programas/listar_programas.html', {'programas': programas})