from django.contrib import admin
from models import *

# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('documento', 'tipo_documento', 'nombre', 'apellido', 'cargo')
    
    
admin.site.register(Empleado, EmpleadoAdmin)