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
        form = CrearAspiranteForm(request.POST)
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
    
   
@login_required
def dashboard(request):
    try:
        aspirante = Aspirante.objects.get(documento=request.user.aspirante.documento)
    except:
        messages.warning(request, "El aspirante no existe.")
        return redirect('home')
    return render(request, 'admisiones/dashboard.html', {'aspirante': aspirante})