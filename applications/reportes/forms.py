# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from django_select2.forms import Select2MultipleWidget, Select2Widget

from admisionesabc.global_variables import *
from models import *
from applications.admisiones.models import *


# PERIODO = 'Febrero-Junio 2017'


class InscritosPorOfertaForm(forms.Form):
    periodo = forms.ModelChoiceField(queryset=Periodo.objects.all(), widget=Select2Widget)
    
    def __init__(self, *args, **kwargs):
        super(InscritosPorOfertaForm, self).__init__(*args, **kwargs)
        
        # Campos de el aspirante
        self.fields['periodo'].widget.attrs.update({'placeholder': 'Seleccione el Periodo', 'required':'required'})
        self.fields['periodo'].label = 'Periodo'