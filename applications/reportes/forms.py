# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from django_select2.forms import Select2MultipleWidget, Select2Widget

from admisionesabc.global_variables import *
from models import *
from applications.admisiones.models import *


# PERIODO = 'Febrero-Junio 2017'


class InscritosPorOfertaForm(forms.Form):
    periodo = forms.ModelChoiceField(queryset=Periodo.objects.all().order_by('identificador'), widget=Select2Widget)
    
    def __init__(self, *args, **kwargs):
        super(InscritosPorOfertaForm, self).__init__(*args, **kwargs)
        
        # Campos de el aspirante
        self.fields['periodo'].widget.attrs.update({'placeholder': 'Seleccione el Periodo', 'required':'required'})
        self.fields['periodo'].label = 'Periodo'
        
        
class InscritosPorFechaForm(forms.Form):
    periodo = forms.ModelChoiceField(queryset=Periodo.objects.all().order_by('identificador'), widget=Select2Widget)
    
    def __init__(self, *args, **kwargs):
        super(InscritosPorFechaForm, self).__init__(*args, **kwargs)
        
        # Campos de el aspirante
        self.fields['periodo'].widget.attrs.update({'placeholder': 'Seleccione el Periodo', 'required':'required'})
        self.fields['periodo'].label = 'Periodo'
        
        
class InscritosPorProgramaForm(forms.Form):
    programa = forms.ModelChoiceField(queryset=Programa.objects.all().order_by('codigo'), widget=Select2Widget)
    
    def __init__(self, *args, **kwargs):
        super(InscritosPorProgramaForm, self).__init__(*args, **kwargs)
        
        # Campos de el aspirante
        self.fields['programa'].widget.attrs.update({'placeholder': 'Seleccione el Programa', 'required':'required'})
        self.fields['programa'].label = 'Programa'