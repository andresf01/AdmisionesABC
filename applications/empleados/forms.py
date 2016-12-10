# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django_select2.forms import Select2MultipleWidget, Select2Widget

from admisionesabc.global_variables import *
from models import *


# PERIODO = 'Febrero-Junio 2017'


class CrearEmpleadoForm(UserCreationForm):
    required_css_class = 'required'
    
    def __init__(self, *args, **kwargs):
        super(CrearEmpleadoForm, self).__init__(*args, **kwargs)
        
        # Campos de usario de django
        self.fields['username'].widget.attrs.update({'placeholder': 'Escriba un nombre de usuario', 'required':'required'})
        self.fields['username'].label = 'Usuario'
        self.fields['username'].help_text = 'Requerido. 30 caracteres o menos. Solamente letras, números y @/./+/-/_'
        self.fields['password1'].widget.attrs.update({'placeholder': 'Escriba una contraseña', 'required':'required'})
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirme la contraseña', 'required':'required'})
        self.fields['password2'].label = 'Confirmar Contraseña'
        self.fields['password2'].help_text = 'Ingrese la misma contraseña de antes, para verificacion.'
        self.fields['email'].widget.attrs.update({'placeholder': 'Escriba su correo electronico', 'label':'Correo Electronico', 'required':'required'})
        self.fields['email'].label = 'Correo Electronico'
        
        # Campos del empleado
        self.fields['documento'].widget.attrs.update({'placeholder': 'Escriba su numero de documento', 'required':'required'})
        self.fields['tipo_documento'].widget.attrs.update({'placeholder': 'Seleccione el tipo de documento', 'required':'required'})
        self.fields['cargo'].widget.attrs.update({'placeholder': 'Seleccione el cargo del empleado', 'required':'required'})
        self.fields['nombre'].widget.attrs.update({'placeholder': 'Escriba su nombre', 'required':'required'})
        self.fields['apellido'].widget.attrs.update({'placeholder': 'Escriba sus apellidos', 'required':'required'})
        self.fields['direccion'].widget.attrs.update({'placeholder': 'Escriba su direccion', 'required':'required'})
        self.fields['telefono'].widget.attrs.update({'placeholder': 'Escriba su telefono', 'required':'required'})


    class Meta:
        model = Empleado
        fields = ('username', 'documento', 'tipo_documento', 'nombre', 'apellido', 'email', 'cargo', 'direccion', 'telefono')
        widgets = {
            'tipo_documento': Select2Widget,
            'cargo': Select2Widget,
        }
        
        
    def clean_documento(self):
        documento = self.cleaned_data['documento']
        if not documento.isdigit():
            raise forms.ValidationError("El numero de documento debe contener solo numeros.")
        return documento
        
    
    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if not telefono.isdigit():
            raise forms.ValidationError("El telefono debe contener solo numeros.")
        return telefono
        
        
class EditarEmpleadoForm(UserChangeForm):
    required_css_class = 'required'
    
    def __init__(self, *args, **kwargs):
        super(EditarEmpleadoForm, self).__init__(*args, **kwargs)
        
        # Campos de usario de django
        self.fields['username'].widget.attrs.update({'placeholder': 'Escriba un nombre de usuario', 'required':'required'})
        self.fields['username'].label = 'Usuario'
        self.fields['username'].help_text = 'Requerido. 30 caracteres o menos. Solamente letras, digitos y @/./+/-/_'
        self.fields['email'].widget.attrs.update({'placeholder': 'Escriba su correo electronico', 'label':'Correo Electronico', 'required':'required'})
        self.fields['email'].label = 'Correo Electronico'
        
        # Campos del empleado
        self.fields['documento'].widget.attrs.update({'placeholder': 'Escriba su numero de documento', 'required':'required'})
        self.fields['tipo_documento'].widget.attrs.update({'placeholder': 'Seleccione el tipo de documento', 'required':'required'})
        self.fields['nombre'].widget.attrs.update({'placeholder': 'Escriba su nombre', 'required':'required'})
        self.fields['apellido'].widget.attrs.update({'placeholder': 'Escriba sus apellidos', 'required':'required'})
        self.fields['direccion'].widget.attrs.update({'placeholder': 'Escriba su direccion', 'required':'required'})
        self.fields['telefono'].widget.attrs.update({'placeholder': 'Escriba su telefono', 'required':'required'})


    class Meta:
        model = Empleado
        fields = ('username', 'documento', 'tipo_documento', 'email', 'cargo', 'nombre', 'apellido', 'direccion', 'telefono',)
        widgets = {
            'tipo_documento': Select2Widget,
            'cargo': Select2Widget,
        }
        
        
    def clean_documento(self):
        documento = self.cleaned_data['documento']
        if not documento.isdigit():
            raise forms.ValidationError("El numero de documento debe contener solo numeros.")
        empleado = None
        try:
            empleado = Empleado.objects.get(documento=documento)
        except Exception:
            pass
        if empleado:
            if self.instance.id != empleado.id:
                raise forms.ValidationError("El numero de documento ya se encuentra registrado.")
        return documento
        
    
    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if not telefono.isdigit():
            raise forms.ValidationError("El telefono debe contener solo numeros.")
        return telefono
        
        
class SetPasswordEmpleadoForm(SetPasswordForm):
    required_css_class = 'required'
    
    def __init__(self, user, *args, **kwargs):
        super(SetPasswordEmpleadoForm, self).__init__(user, *args, **kwargs)
        
        # Campos de formulario de django
        self.fields['new_password1'].widget.attrs.update({'placeholder': 'Escriba una contraseña', 'required':'required'})
        self.fields['new_password1'].label = 'Contraseña'
        self.fields['new_password1'].help_text = "<ul><li>Tu contraseña no puede ser similar a otra información personal.</li><li>Tu contraseña debe contener al menos 8 caracteres.</li><li>Tu contraseña no puede ser común.</li><li>Tu contraseña no puede ser sólo numérica.</li></ul>"
        self.fields['new_password2'].widget.attrs.update({'placeholder': 'Confirme la contraseña', 'required':'required'})
        self.fields['new_password2'].label = 'Confirmar Contraseña'
        self.fields['new_password2'].help_text = 'Ingrese la misma contraseña de antes, para verificacion.'