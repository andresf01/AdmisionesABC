# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from django.conf import settings
from django_select2.forms import Select2MultipleWidget, Select2Widget
import urllib
import urllib2
import json

from admisionesabc.global_variables import *
from models import *


# PERIODO = 1


class CrearAspiranteForm(ModelForm):
    required_css_class = 'required'
    # confirm_password = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={'placeholder':'Confirme su contraseña', 'required':'required'}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CrearAspiranteForm, self).__init__(*args, **kwargs)
        
        puntaje_minimo = None
        try:
            puntaje_minimo = Periodo.objects.get(id=PERIODO).puntaje_minimo
        except Exception as ex:
            print ex.message
        
        # self.fields['username'].widget.attrs.update({'placeholder': 'Escriba un nombre de usuario', 'required':'required'})
        # self.fields['username'].label = 'Usuario'
        # self.fields['password'].widget.attrs.update({'placeholder': 'Escriba una contraseña', 'required':'required'})
        # self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': 'Escriba una contraseña', 'required':'required'})
        # self.fields['password'].label = 'Contraseña'
        # Campos de usario de django
        self.fields['email'].widget.attrs.update({'placeholder': 'Escriba su correo electronico', 'label':'Correo Electronico', 'required':'required'})
        self.fields['email'].label = 'Correo Electronico'
        
        # Campos de el aspirante
        self.fields['documento'].widget.attrs.update({'placeholder': 'Escriba su número de documento', 'required':'required'})
        self.fields['tipo_documento'].widget.attrs.update({'placeholder': 'Seleccione el tipo de documento', 'required':'required'})
        self.fields['snp'].widget.attrs.update({'placeholder': 'Escriba el SNP de su examen ICFES', 'required':'required'})
        self.fields['puntaje_global'].widget.attrs.update({'placeholder': 'Escriba su puntaje global', 'min':puntaje_minimo, 'required':'required'})
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
        widgets = {
            'tipo_documento': Select2Widget,
            'programa': Select2Widget,
        }
        
    
    def clean_documento(self):
        documento = self.cleaned_data['documento']
        if not documento.isdigit():
            raise forms.ValidationError("El numero de documento debe contener solo numeros.")
        # ofertas = Periodo.objects.get(id=PERIODO).oferta_set.all()
        # for oferta in ofertas:
        #     aspirante = None
        #     try:
        #         aspirante = oferta.aspirante_set.get(documento=documento)
        #     except Exception:
        #         pass
        #     if aspirante:
        #         raise forms.ValidationError("Este numero de documento ya se encuentra registrado en este periodo de admisiones.")
        aspirante = None
        try:
            aspirante = Aspirante.objects.get(programa__periodo__id=PERIODO, documento=documento)
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
        # ofertas = Periodo.objects.get(id=PERIODO).oferta_set.all()
        # for oferta in ofertas:
        #     aspirante = None
        #     try:
        #         aspirante = oferta.aspirante_set.get(snp=snp)
        #     except Exception:
        #         pass
        #     if aspirante:
        #         raise forms.ValidationError("Este Icfes SNP ya se encuentra registrado en este periodo de admisiones.")
        aspirante = None
        try:
            aspirante = Aspirante.objects.get(programa__periodo__id=PERIODO, snp=snp)
        except Exception:
            pass
        if aspirante:
            raise forms.ValidationError("Este Icfes SNP ya se encuentra registrado en este periodo de admisiones.")
        return snp
        
    def clean(self):
        super(CrearAspiranteForm, self).clean()

        # test the google recaptcha
        url = "https://www.google.com/recaptcha/api/siteverify"
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': self.request.POST.get(u'g-recaptcha-response', None),
            'remoteip': self.request.META.get("REMOTE_ADDR", None),
        }
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        result = json.loads(response.read())

        # result["success"] will be True on a success
        if not result["success"]:
            raise forms.ValidationError(u'Error al procesar el captcha.')

        return self.cleaned_data
 
       
class EditarAspiranteForm(ModelForm):
    required_css_class = 'required'

    def __init__(self, *args, **kwargs):
        super(EditarAspiranteForm, self).__init__(*args, **kwargs)
        
        puntaje_minimo = None
        try:
            puntaje_minimo = Periodo.objects.get(id=PERIODO).puntaje_minimo
        except Exception as ex:
            print ex.message

        # Campos de usario de django
        self.fields['email'].widget.attrs.update({'placeholder': 'Escriba su correo electronico', 'label': 'Correo Electrónico', 'required': 'required'})
        self.fields['email'].label = 'Correo Electronico'
        
        # Campos de el aspirante
        self.fields['documento'].widget.attrs.update({'placeholder': 'Escriba su numero de documento', 'required': 'required'})
        self.fields['tipo_documento'].widget.attrs.update({'placeholder': 'Seleccione el tipo de documento', 'required': 'required'})
        self.fields['snp'].widget.attrs.update({'placeholder': 'Escriba el SNP de su examen ICFES', 'required': 'required'})
        self.fields['puntaje_global'].widget.attrs.update({'placeholder': 'Escriba su puntaje global', 'min': puntaje_minimo, 'required': 'required'})
        self.fields['colegio'].widget.attrs.update({'placeholder': 'Escriba el nombre de su colegio', 'required': 'required'})
        self.fields['nombre'].widget.attrs.update({'placeholder': 'Escriba su nombre', 'required': 'required'})
        self.fields['apellido'].widget.attrs.update({'placeholder': 'Escriba sus apellidos', 'required': 'required'})
        self.fields['direccion'].widget.attrs.update({'placeholder': 'Escriba su direccion', 'required': 'required'})
        self.fields['telefono'].widget.attrs.update({'placeholder': 'Escriba su telefono', 'required': 'required'})
        self.fields['programa'].widget.attrs.update({'placeholder': 'Seleccione el programa al que desea ingresar', 'required': 'required'})
        self.fields['programa'].queryset = Oferta.objects.filter(periodo_id=PERIODO)


    class Meta:
        model = Aspirante
        fields = ('documento', 'tipo_documento', 'snp', 'puntaje_global', 'colegio', 'nombre', 'apellido', 'email', 'direccion', 'telefono', 'programa', 'ponderado', 'admitido', 'nota_admision')
        widgets = {
            'tipo_documento': Select2Widget,
            'programa': Select2Widget,
        }
        
    
    def clean_documento(self):
        documento = self.cleaned_data['documento']
        if not documento.isdigit():
            raise forms.ValidationError("El numero de documento debe contener solo numeros.")
        # ofertas = Periodo.objects.get(id=PERIODO).oferta_set.all()
        # for oferta in ofertas:
        #     aspirante = None
        #     try:
        #         aspirante = oferta.aspirante_set.get(documento=documento)
        #     except Exception:
        #         pass
        #     if aspirante:
        #         if self.instance.id != aspirante.id:
        #             raise forms.ValidationError("Este numero de documento ya se encuentra registrado en este periodo de admisiones.")
        aspirante = None
        try:
            aspirante = Aspirante.objects.get(programa__periodo__id=PERIODO, documento=documento)
        except Exception:
            pass
        if aspirante:
            if self.instance.id != aspirante.id:
                raise forms.ValidationError("Este numero de documento ya se encuentra registrado en este periodo de admisiones.")
        return documento
        
    
    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if not telefono.isdigit():
            raise forms.ValidationError("El telefono debe contener solo numeros.")
        return telefono
        
        
    def clean_snp(self):
        snp = self.cleaned_data['snp']
        # ofertas = Periodo.objects.get(id=PERIODO).oferta_set.all()
        # for oferta in ofertas:
        #     aspirante = None
        #     try:
        #         aspirante = oferta.aspirante_set.get(snp=snp)
        #     except Exception:
        #         pass
        #     if aspirante:
        #         if self.instance.id != aspirante.id:
        #             raise forms.ValidationError("Este Icfes SNP ya se encuentra registrado en este periodo de admisiones.")
        aspirante = None
        try:
            aspirante = Aspirante.objects.get(programa__periodo__id=PERIODO, snp=snp)
        except Exception:
            pass
        if aspirante:
            if self.instance.id != aspirante.id:
                raise forms.ValidationError("Este Icfes SNP ya se encuentra registrado en este periodo de admisiones.")
        return snp
        
class CrearPeriodoForm(ModelForm):
    required_css_class = 'required'

    def __init__(self, *args, **kwargs):
        super(CrearPeriodoForm, self).__init__(*args, **kwargs)
        
        self.fields['identificador'].widget.attrs.update({'placeholder': 'Escriba el identificador ', 'required':'required'})
        self.fields['nombre'].widget.attrs.update({'placeholder': 'Escriba el nombre del periodo', 'required':'required'})
        self.fields['puntaje_minimo'].widget.attrs.update({'placeholder': 'Escriba el puntaje minimo de inscripcion del periodo', 'min':0, 'required':'required'})
        
        
    class Meta:
        model = Periodo
        fields = ('identificador', 'nombre', 'puntaje_minimo')
        exclude = ('programas', 'activo', 'hay_resultados')
        
        
    def clean_identificador(self):
        identificador = self.cleaned_data['identificador']
        periodo = None
        try:
            periodo = Periodo.objects.get(identificador=identificador)
        except Exception:
            pass
        if periodo:
            raise forms.ValidationError("Este identificador de periodo ya se encuentra registrado.")
        return identificador
    
    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        periodo = None
        try:
            periodo = Periodo.objects.get(nombre=nombre)
        except Exception:
            pass
        if periodo:
            raise forms.ValidationError("Este nombre de periodo ya se encuentra registrado.")
        return nombre
        
        
class EditarPeriodoForm(ModelForm):
    required_css_class = 'required'

    def __init__(self, *args, **kwargs):
        super(EditarPeriodoForm, self).__init__(*args, **kwargs)
        
        self.fields['nombre'].widget.attrs.update({'placeholder': 'Escriba el nombre del periodo', 'required':'required'})
        self.fields['puntaje_minimo'].widget.attrs.update({'placeholder': 'Escriba el puntaje minimo de inscripcion del periodo', 'min':0, 'required':'required'})
        
        
    class Meta:
        model = Periodo
        fields = ('identificador', 'nombre', 'puntaje_minimo', 'activo', 'hay_resultados')
        exclude = ('programas',)
        
        
    def clean_identificador(self):
        identificador = self.cleaned_data['identificador']
        periodo = None
        try:
            periodo = Periodo.objects.get(identificador=identificador)
        except Exception:
            pass
        if periodo:
            if self.instance != periodo:
                raise forms.ValidationError("Este identificador de periodo ya se encuentra registrado.")
        return identificador
    
    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        periodo = None
        try:
            periodo = Periodo.objects.get(nombre=nombre)
        except Exception as ex:
            print ex.message
        if periodo:
            if self.instance != periodo:
                raise forms.ValidationError("Este nombre de periodo ya se encuentra registrado.")
        return nombre
        
        
    def clean_activo(self):
        activo = self.cleaned_data['activo']
        if activo:
            periodo = None
            try:
                periodo = Periodo.objects.get(activo=True)
            except Exception as ex:
                print ex.message
            if periodo:
                if self.instance != periodo:
                    raise forms.ValidationError("Solo debe de existir un periodo activo a la vez.")
        return activo
            
        
        
class CrearCalendarioForm(ModelForm):
    required_css_class = 'required'

    def __init__(self, *args, **kwargs):
        super(CrearCalendarioForm, self).__init__(*args, **kwargs)
        
        self.fields['nombre'].widget.attrs.update({'placeholder': 'Escriba el nombre del calendario', 'required':'required'})
        self.fields['descripcion'].widget = forms.Textarea(attrs={'placeholder': 'Escriba una descripcion del calendario', 'required':'required'})
        self.fields['periodo'].widget.attrs.update({'placeholder': 'Seleccione el periodo del calendario', 'required':'required'})
        self.fields['periodo'].queryset = Periodo.objects.filter(id=None)
        
        
    class Meta:
        model = Calendario
        fields = ('nombre', 'descripcion', 'periodo')
        
        
    def clean_periodo(self):
        periodo = self.cleaned_data['periodo']
        if hasattr(periodo, 'calendario'):
            raise forms.ValidationError("Este periodo ya tiene un calendario asignado.")
        return periodo
        

class CrearEventoForm(ModelForm):
    required_css_class = 'required'

    def __init__(self, *args, **kwargs):
        super(CrearEventoForm, self).__init__(*args, **kwargs)
        
        self.fields['titulo'].widget.attrs.update({'placeholder': 'Escriba el titulo del evento', 'required':'required'})
        self.fields['descripcion'].widget = forms.Textarea(attrs={'placeholder': 'Escriba la descripcion del evento', 'required':'required'})
        self.fields['calendario'].widget.attrs.update({'placeholder': 'Seleccione el periodo del calendario', 'required':'required'})
        self.fields['calendario'].queryset = Calendario.objects.all()
        
        
    class Meta:
        model = Evento
        fields = ('titulo', 'descripcion', 'calendario')
        
        
class CrearOfertaForm(ModelForm):
    required_css_class = 'required'
    
    def __init__(self, *args, **kwargs):
        super(CrearOfertaForm, self).__init__(*args, **kwargs)
        
        self.fields['periodo'].widget.attrs.update({'placeholder': 'Seleccione el programa al que desea ingresar', 'required': 'required'})
        self.fields['periodo'].queryset = Periodo.objects.all()
        self.fields['programa'].widget.attrs.update({'placeholder': 'Seleccione el programa al que desea ingresar', 'required': 'required'})
        self.fields['programa'].queryset = Programa.objects.all()
        self.fields['cupo'].widget.attrs.update({'placeholder': 'Ingrese el cupo del programa académico', 'min': 0, 'required': 'required'})
        self.fields['peso_lectura'].widget.attrs.update({'placeholder': 'Ingrese el peso de lectura crítica', 'min': 0, 'max': 100, 'required': 'required'})
        self.fields['peso_matematicas'].widget.attrs.update({'placeholder': 'Ingrese el peso de matematicas', 'min': 0, 'max': 100, 'required': 'required'})
        self.fields['peso_naturales'].widget.attrs.update({'placeholder': 'Ingrese el peso de ciencias naturales', 'min': 0, 'max': 100, 'required': 'required'})
        self.fields['peso_sociales'].widget.attrs.update({'placeholder': 'Ingrese el peso de ciencias sociales', 'min': 0, 'max': 100, 'required': 'required'})
        self.fields['peso_ingles'].widget.attrs.update({'placeholder': 'Ingrese el peso de ingles', 'min': 0, 'max': 100, 'required': 'required'})
        self.fields['peso_prueba'].widget.attrs.update({'placeholder': 'Ingrese el peso de prueba específica', 'min': 0, 'max': 100, 'required': 'required'})
        
        
    class Meta:
        model = Oferta
        fields = ('periodo', 'programa', 'cupo', 'peso_lectura', 'peso_matematicas', 'peso_naturales', 'peso_sociales', 'peso_ingles', 'peso_prueba')
        widgets = {
            'periodo': Select2Widget,
            'programa': Select2Widget,
        }
        
        
    def clean(self):
        periodo = self.cleaned_data.get('periodo')
        programa = self.cleaned_data.get('programa')
        oferta = None
        try:
            oferta = Oferta.objects.get(periodo_id=periodo.id, programa_id=programa.id)
        except Exception:
            pass
        if oferta:
            raise forms.ValidationError('Este programa academico ya se encuentra ofertado en este periodo de admisiones')
        
        peso_lectura = self.cleaned_data.get('peso_lectura')
        peso_matematicas = self.cleaned_data.get('peso_matematicas')
        peso_naturales = self.cleaned_data.get('peso_naturales')
        peso_sociales = self.cleaned_data.get('peso_sociales')
        peso_ingles = self.cleaned_data.get('peso_ingles')
        peso_prueba = self.cleaned_data.get('peso_prueba')
        total = peso_lectura + peso_matematicas + peso_naturales + peso_sociales + peso_ingles + peso_prueba
        if total != 100:
            raise forms.ValidationError('El total de los pesos debe ser exactamente igual a 100.')
            
        return self.cleaned_data
        
        
class EditarOfertaForm(ModelForm):
    required_css_class = 'required'
    
    def __init__(self, *args, **kwargs):
        super(EditarOfertaForm, self).__init__(*args, **kwargs)
        
        # self.fields['periodo'].widget.attrs.update({'placeholder': 'Seleccione el programa al que desea ingresar', 'required': 'required'})
        # self.fields['periodo'].queryset = Periodo.objects.all()
        # self.fields['programa'].widget.attrs.update({'placeholder': 'Seleccione el programa al que desea ingresar', 'required': 'required'})
        # self.fields['programa'].queryset = Programa.objects.all()
        self.fields['cupo'].widget.attrs.update({'placeholder': 'Ingrese el cupo del programa académico', 'min': 0, 'required': 'required'})
        self.fields['peso_lectura'].widget.attrs.update({'placeholder': 'Ingrese el peso de lectura crítica', 'min': 0, 'max': 100, 'required': 'required'})
        self.fields['peso_matematicas'].widget.attrs.update({'placeholder': 'Ingrese el peso de matematicas', 'min': 0, 'max': 100, 'required': 'required'})
        self.fields['peso_naturales'].widget.attrs.update({'placeholder': 'Ingrese el peso de ciencias naturales', 'min': 0, 'max': 100, 'required': 'required'})
        self.fields['peso_sociales'].widget.attrs.update({'placeholder': 'Ingrese el peso de ciencias sociales', 'min': 0, 'max': 100, 'required': 'required'})
        self.fields['peso_ingles'].widget.attrs.update({'placeholder': 'Ingrese el peso de ingles', 'min': 0, 'max': 100, 'required': 'required'})
        self.fields['peso_prueba'].widget.attrs.update({'placeholder': 'Ingrese el peso de prueba específica', 'min': 0, 'max': 100, 'required': 'required'})
        
        
    class Meta:
        model = Oferta
        fields = ('cupo', 'peso_lectura', 'peso_matematicas', 'peso_naturales', 'peso_sociales', 'peso_ingles', 'peso_prueba')
        
        
    def clean(self):
        peso_lectura = self.cleaned_data.get('peso_lectura')
        peso_matematicas = self.cleaned_data.get('peso_matematicas')
        peso_naturales = self.cleaned_data.get('peso_naturales')
        peso_sociales = self.cleaned_data.get('peso_sociales')
        peso_ingles = self.cleaned_data.get('peso_ingles')
        peso_prueba = self.cleaned_data.get('peso_prueba')
        total = peso_lectura + peso_matematicas + peso_naturales + peso_sociales + peso_ingles + peso_prueba
        if total != 100:
            raise forms.ValidationError('El total de los pesos debe ser exactamente igual a 100.')
            
        return self.cleaned_data 
        