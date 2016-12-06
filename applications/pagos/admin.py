from django.contrib import admin

from models import *

# Register your models here.


class PagoAdmin(admin.ModelAdmin):
    list_display = ('aspirante', 'pagado')
    
    
admin.site.register(Pago, PagoAdmin)