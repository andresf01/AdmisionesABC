# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate


# class LoginForm(AuthenticationForm):
#     username = forms.CharField(label='Usuario', widget=forms.TextInput(attrs={'placeholder':'Usuario', 'required':'required'})) 
#     password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'placeholder':'Contraseña', 'required':'required'}))
    
    
class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', widget=forms.TextInput(attrs={'placeholder':'Usuario', 'required':'required', 'class':'form-control'})) 
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'placeholder':'Contraseña', 'required':'required', 'class':'form-control'}))
    
    error_messages = {
        'invalid_login': ("Usuario o Contraseña incorrectos."),
        'inactive': ("La cuenta esta desactivada."),
    }
    
    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                )
            else:
                if not self.user_cache.is_active:
                    raise forms.ValidationError(
                        self.error_messages['inactive'],
                        code='inactive',
                    )

        return self.cleaned_data
        
    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache