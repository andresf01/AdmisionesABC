from django.contrib import admin

from models import *

# Register your models here.


class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('identificador', 'nombre', 'puntaje_minimo', 'activo', 'hay_resultados')
    
    
class OfertaAdmin(admin.ModelAdmin):
    list_display = ('periodo', 'programa', 'cupo')
    
    
class AspiranteAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_joined', 'documento', 'tipo_documento', 'nombre', 'apellido', 'snp', 'puntaje_global')
    

admin.site.register(Periodo, PeriodoAdmin)
admin.site.register(Calendario)
admin.site.register(Evento)
admin.site.register(Oferta, OfertaAdmin)
admin.site.register(Aspirante, AspiranteAdmin)