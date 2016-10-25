from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

from forms import *
from models import *
from applications.admisiones.models import *

# Create your views here.

PERIODO = 'Febrero-Junio 2017'


def programas(request):
    programas = Programa.objects.all()
    return render(request, 'programas/programas.html', {'programas': programas})
    
    
def programa(request, programa_id):
    try:
        programa = Programa.objects.get(codigo=programa_id)
        oferta = Oferta.objects.get(programa_id=programa.id, periodo_id=PERIODO)
    except Exception:
        messages.warning(request, "El programa o la oferta no existen.")
        return redirect('programas')

    return render(request, 'programas/programa.html', {'programa': programa, 'oferta': oferta})
    

@login_required
def crear_programa(request):
    form = ProgramaForm()
    if request.method == 'POST':
        form = ProgramaForm(request.POST)
        if form.is_valid():
            programa = form.save()
            return redirect('listar_programas')

    return render(request, 'programas/crear_programa.html', {'form': form})
    
    
@login_required
def editar_programa(request, programa_id):
    try:
        programa = Programa.objects.get(codigo=programa_id)
    except Exception:
        return redirect('listar_programas')

    # instance e initial para cargar datos en los campos
    form = ProgramaForm(instance=programa, initial=programa.__dict__)
    if request.method == 'POST':
        form = ProgramaForm(request.POST, instance=programa, initial=programa.__dict__)
        if form.is_valid():
            programa = form.save(commit=False)
            programa.save()
            messages.success(request, "Programa modificado correctamente.")
            return redirect('listar_programas')

    return render(request, 'programas/editar_programa.html', {'form': form})
    
    
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
    programas = Programas.objects.all()
    return render(request, 'programas/listar_programas.html', {'programas': programas})