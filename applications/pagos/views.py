from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group, Permission
import urllib

from models import *
from forms import *

# Create your views here.


def realizar_pago(request, pago_id):
    values = {
        'order_id': pago_id,
        'amount': 40000,
    }
    return custom_redirect('https://secure-payments-online-camilo1090.c9users.io/payments/pay', values)
    

def custom_redirect(url, values):
    data = urllib.urlencode(values)
    return HttpResponseRedirect(url + "?%s" % data)
    
    
def online(request):
    html = 'this message should never show up'
    if request.method == 'GET':
        pago_id = request.GET['order_id']
        try:
            pago = Pago.objects.get(id=pago_id)
            pago.pagado = True
            pago.save()
            html = 'OK'
        except Exception as ex:
            print ex.message
            html = 'ERROR'
            
    return HttpResponse(html)
    
    
@login_required
def listar_pagos(request):
    pagos = Pago.objects.all()
    return render(request, 'pagos/listar_pagos.html', {'pagos': pagos, 'nombre_periodo': 'TODOS LOS PERIODOS'})
    
    
@login_required
def listar_pagos_periodo(request, periodo_id):
    try:
        periodo = Periodo.objects.get(identificador=periodo_id)
        pagos = Pago.objects.filter(aspirante__programa__periodo__id=periodo.id)
        return render(request, 'pagos/listar_pagos.html', {'pagos': pagos, 'periodo': periodo.nombre})
    except Exception as ex:
        print ex.message
        return redirect('listar_periodos')
        
        
@login_required
def editar_pago(request, pago_id):
    try:
        pago = Pago.objects.get(id=pago_id)
    except Exception:
        return redirect('listar_periodos')

    # instance e initial para cargar datos en los campos
    form = EditarPagoForm(instance=pago, initial=pago.__dict__)
    if request.method == 'POST':
        form = EditarPagoForm(request.POST, instance=pago, initial=pago.__dict__)
        if form.is_valid():
            pago = form.save()
            messages.success(request, "Pago modificado correctamente.")
            return redirect('listar_pagos')
        messages.error(request, "Error al modificar el pago.")

    return render(request, 'pagos/editar_pago.html', {'form': form})
    
