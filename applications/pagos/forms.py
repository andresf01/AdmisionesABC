# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from django_select2.forms import Select2MultipleWidget, Select2Widget

from admisionesabc.global_variables import *
from models import *


# PERIODO = 'Febrero-Junio 2017'
        
        
class EditarPagoForm(ModelForm):
    required_css_class = 'required'

    def __init__(self, *args, **kwargs):
        super(EditarPagoForm, self).__init__(*args, **kwargs)
        
        self.fields['aspirante'].widget.attrs.update({'placeholder': 'Seleccione el aspirante relacionado con el pago', 'required': 'required'})


    class Meta:
        model = Pago
        fields = ('aspirante', 'pagado')
        widgets = {
            'aspirante': Select2Widget,
        }
        
        
    def clean_aspirante(self):
        aspirante = self.cleaned_data['aspirante']
        if hasattr(aspirante, 'pago'):
            if aspirante.pago != self.instance:
                raise forms.ValidationError("El estudiante seleccionado ya tiene un pago asociado.")
        return aspirante