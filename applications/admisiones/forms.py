# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from models import *


PERIODO = 'Febrero-Junio 2017'


class CrearAspiranteForm(ModelForm):
    required_css_class = 'required'
    # confirm_password = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={'placeholder':'Confirme su contraseña', 'required':'required'}))

    def __init__(self, *args, **kwargs):
        super(CrearAspiranteForm, self).__init__(*args, **kwargs)
        
        # self.fields['username'].widget.attrs.update({'placeholder': 'Escriba un nombre de usuario', 'required':'required'})
        # self.fields['username'].label = 'Usuario'
        # self.fields['password'].widget.attrs.update({'placeholder': 'Escriba una contraseña', 'required':'required'})
        # self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': 'Escriba una contraseña', 'required':'required'})
        # self.fields['password'].label = 'Contraseña'
        # Campos de usario de django
        self.fields['email'].widget.attrs.update({'placeholder': 'Escriba su correo electronico', 'label':'Correo Electronico', 'required':'required'})
        self.fields['email'].label = 'Correo Electronico'
        
        # Campos de el aspirante
        self.fields['documento'].widget.attrs.update({'placeholder': 'Escriba su numero de documento', 'required':'required'})
        self.fields['tipo_documento'].widget.attrs.update({'placeholder': 'Seleccione el tipo de documento', 'required':'required'})
        self.fields['snp'].widget.attrs.update({'placeholder': 'Escriba el SNP de su examen ICFES', 'required':'required'})
        self.fields['puntaje_global'].widget.attrs.update({'placeholder': 'Escriba su puntaje global', 'min':Periodo.objects.get(periodo=PERIODO).puntaje_minimo, 'required':'required'})
        self.fields['colegio'].widget.attrs.update({'placeholder': 'Escriba el nombre de su colegio', 'required':'required'})
        self.fields['nombre'].widget.attrs.update({'placeholder': 'Escriba su nombre', 'required':'required'})
        self.fields['apellido'].widget.attrs.update({'placeholder': 'Escriba sus apellidos', 'required':'required'})
        self.fields['direccion'].widget.attrs.update({'placeholder': 'Escriba su direccion', 'required':'required'})
        self.fields['telefono'].widget.attrs.update({'placeholder': 'Escriba su telefono', 'required':'required'})
        self.fields['programa'].widget.attrs.update({'placeholder': 'Seleccione el programa al que desea ingresar', 'required':'required'})
        self.fields['programa'].queryset = Oferta.objects.filter(periodo_id=PERIODO)


    class Meta:
        model = Aspirante
        fields = ('documento', 'tipo_documento', 'snp', 'puntaje_global', 'colegio', 'nombre', 'apellido', 'email', 'direccion', 'telefono', 'programa')
        # widgets = {
        #     'documento':forms.NumberInput(),
        # }
        
    
    def clean_documento(self):
        documento = self.cleaned_data['documento']
        if not documento.isdigit():
            raise forms.ValidationError("El numero de documento debe contener solo numeros.")
        ofertas = Periodo.objects.get(periodo=PERIODO).oferta_set.all()
        for oferta in ofertas:
            aspirante = None
            try:
                aspirante = oferta.aspirante_set.get(documento=documento)
            except Exception:
                pass
            if aspirante:
                raise forms.ValidationError("Este numero de documento ya se encuentra registrado en este periodo de admisiones.")
        return documento
        
    
    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if not telefono.isdigit():
            raise forms.ValidationError("El telefono debe contener solo numeros.")
        return telefono
        
        
    def clean_snp(self):
        snp = self.cleaned_data['snp']
        ofertas = Periodo.objects.get(periodo=PERIODO).oferta_set.all()
        for oferta in ofertas:
            aspirante = None
            try:
                aspirante = oferta.aspirante_set.get(snp=snp)
            except Exception:
                pass
            if aspirante:
                raise forms.ValidationError("Este Icfes SNP ya se encuentra registrado en este periodo de admisiones.")
        return snp
        