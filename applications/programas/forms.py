# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from models import *


PERIODO = 'Febrero-Junio 2017'


class ProgramaForm(ModelForm):
    required_css_class = 'required'

    def __init__(self, *args, **kwargs):
        super(CrearProgramaForm, self).__init__(*args, **kwargs)
        
        self.fields['codigo'].widget.attrs.update({'placeholder': 'Escriba el codigo del programa academico', 'required': 'required'})
        self.fields['nombre'].widget.attrs.update({'placeholder': 'Escriba el nombre del programa academico', 'required': 'required'})
        self.fields['snies'].widget.attrs.update({'placeholder': 'Escriba el registro SNIES del programa academico', 'required': 'required'})
        self.fields['creditos'].widget.attrs.update({'placeholder': 'Escriba el numero de creditos del programa academico', 'min': 0, 'required': 'required'})
        self.fields['formacion'].widget.attrs.update({'placeholder': 'Seleccione el tipo de formacion del programa academico', 'required': 'required'})
        self.fields['tipo'].widget.attrs.update({'placeholder': 'Seleccione el tipo del programa academico', 'required': 'required'})
        self.fields['metodologia'].widget.attrs.update({'placeholder': 'Seleccione la metodologia del programa academico', 'required': 'required'})
        self.fields['titulo'].widget.attrs.update({'placeholder': 'Escriba el titulo que otorga el programa academico', 'required': 'required'})


    class Meta:
        model = Programa
        fields = ('codigo', 'nombre', 'snies', 'creditos', 'formacion', 'tipo', 'metodologia', 'titulo',)
        
        
    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']
        programa = Programa.objects.get(codigo=codigo)
        if programa:
            raise forms.ValidationError("Ya existe un programa con el codigo proporcionado.")
        return codigo