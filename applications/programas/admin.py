from django.contrib import admin

from models import *

# Register your models here.


class ProgramaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'snies', 'creditos', 'tipo')
    
    
admin.site.register(Programa, ProgramaAdmin)
