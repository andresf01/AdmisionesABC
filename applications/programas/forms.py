# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from django_select2.forms import Select2MultipleWidget, Select2Widget

from admisionesabc.global_variables import *
from models import *


# PERIODO = 'Febrero-Junio 2017'


class CrearProgramaForm(ModelForm):
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
        self.fields['descripcion'].widget = forms.Textarea(attrs={'placeholder': 'Escriba una descripcion del programa academico', 'required': 'required'})
        self.fields['image_url'].widget.attrs.update({'placeholder': 'Ingrese la url interna de la imagen del programa academico', 'required': 'required'})


    class Meta:
        model = Programa
        fields = ('codigo', 'nombre', 'snies', 'creditos', 'formacion', 'tipo', 'metodologia', 'titulo', 'descripcion', 'image_url')
        widgets = {
            'formacion': Select2Widget,
            'tipo': Select2Widget,
            'metodologia': Select2Widget,
        }
        
        
    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']
        programa = None
        try:
            programa = Programa.objects.get(codigo=codigo)
        except Exception as ex:
            print ex.message
        if programa:
            raise forms.ValidationError("Ya existe un programa con el codigo proporcionado.")
        return codigo
        
        
class EditarProgramaForm(ModelForm):
    required_css_class = 'required'

    def __init__(self, *args, **kwargs):
        super(EditarProgramaForm, self).__init__(*args, **kwargs)
        
        self.fields['codigo'].widget.attrs.update({'placeholder': 'Escriba el codigo del programa academico', 'required': 'required'})
        self.fields['nombre'].widget.attrs.update({'placeholder': 'Escriba el nombre del programa academico', 'required': 'required'})
        self.fields['snies'].widget.attrs.update({'placeholder': 'Escriba el registro SNIES del programa academico', 'required': 'required'})
        self.fields['creditos'].widget.attrs.update({'placeholder': 'Escriba el numero de creditos del programa academico', 'min': 0, 'required': 'required'})
        self.fields['formacion'].widget.attrs.update({'placeholder': 'Seleccione el tipo de formacion del programa academico', 'required': 'required'})
        self.fields['tipo'].widget.attrs.update({'placeholder': 'Seleccione el tipo del programa academico', 'required': 'required'})
        self.fields['metodologia'].widget.attrs.update({'placeholder': 'Seleccione la metodologia del programa academico', 'required': 'required'})
        self.fields['titulo'].widget.attrs.update({'placeholder': 'Escriba el titulo que otorga el programa academico', 'required': 'required'})
        self.fields['descripcion'].widget = forms.Textarea(attrs={'placeholder': 'Escriba una descripcion del programa academico', 'required': 'required'})
        self.fields['image_url'].widget.attrs.update({'placeholder': 'Ingrese la url interna de la imagen del programa academico', 'required': 'required'})


    class Meta:
        model = Programa
        fields = ('codigo', 'nombre', 'snies', 'creditos', 'formacion', 'tipo', 'metodologia', 'titulo', 'descripcion', 'image_url')
        widgets = {
            'formacion': Select2Widget,
            'tipo': Select2Widget,
            'metodologia': Select2Widget,
        }
        
        
    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']
        programa = None
        try:
            programa = Programa.objects.get(codigo=codigo)
        except Exception as ex:
            print ex.message
        if programa:
            if programa != self.instance:
                raise forms.ValidationError("Ya existe un programa con el codigo proporcionado.")
        return codigo