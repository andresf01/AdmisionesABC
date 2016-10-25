# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, Group, Permission

from forms import *
import applications.admisiones.views as views

# Create your views here.

def home(request):
    # print Group.objects.get(name='Aspirante').user_set.all()
    return render(request, 'init/index.html')

def custom_login(request):
    if request.user.is_authenticated():
        return redirect_to_dashboard(request)
    
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)  # se autentican los datos ingresados por el usuario
        if form.is_valid(): # si son validos el form tiene el objeto usuario
            user = form.get_user()
            login(request, user)    # se loguea al usuario
            return redirect_to_dashboard(request)
        
    return render(request, 'init/login.html', {'form': form})
    
    
def redirect_to_dashboard(request):
    if request.user.is_authenticated():
        if hasattr(request.user, 'empleado'):
            return redirect('administrador')
        else:
            return redirect('admisiones_dashboard')