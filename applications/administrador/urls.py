from django.conf.urls import url

import views
import applications.empleados.views as empleados_views
import applications.programas.views as programas_views
import applications.admisiones.views as admisiones_views
import applications.reportes.views as reportes_views
import applications.pagos.views as pagos_views

# urls administrador

urlpatterns = [
    url(r'^$', views.dashboard, name='administrador'),
    
    url(r'^empleados/crear-empleado/', empleados_views.crear_empleado, name='crear_empleado'),
    url(r'^empleados/editar-empleado/(?P<empleado_id>\d+)/', empleados_views.editar_empleado, name='editar_empleado'),
    url(r'^empleados/setpassword-empleado/(?P<empleado_id>\d+)/', empleados_views.setpassword_empleado, name='setpassword_empleado'),
    url(r'^empleados/ver-empleado/(?P<empleado_id>\d+)/', empleados_views.ver_empleado, name='ver_empleado'),
    url(r'^empleados/listar-empleados/', empleados_views.listar_empleados, name='listar_empleados'),
    
    url(r'^programas/crear-programa/', programas_views.crear_programa, name='crear_programa'),
    url(r'^programas/editar-programa/(?P<programa_id>\d+)/', programas_views.editar_programa, name='editar_programa'),
    url(r'^programas/ver-programa/(?P<programa_id>\d+)/', programas_views.ver_programa, name='ver_programa'),
    url(r'^programas/listar-programas/', programas_views.listar_programas, name='listar_programas'),
    
    url(r'^periodos/crear-periodo/', admisiones_views.crear_periodo, name='crear_periodo'),
    url(r'^periodos/editar-periodo/(?P<periodo_id>.+)/', admisiones_views.editar_periodo, name='editar_periodo'),
    # url(r'^periodos/ver-periodo/(?P<periodo_id>.+)/', periodos_views.ver_periodo, name='ver_periodo'),
    url(r'^periodos/listar-periodos/', admisiones_views.listar_periodos, name='listar_periodos'),
    
    url(r'^periodos/crear-oferta/', admisiones_views.crear_oferta, name='crear_oferta'),
    url(r'^periodos/editar-oferta/(?P<oferta_id>.+)/', admisiones_views.editar_oferta, name='editar_oferta'),
    
    url(r'^periodos/listar-aspirantes/(?P<periodo_id>.+)/', admisiones_views.listar_aspirantes_periodo, name='listar_aspirantes_periodo'),
    url(r'^periodos/listar-aspirantes/', admisiones_views.listar_aspirantes, name='listar_aspirantes'),
    url(r'^periodos/listar-oferta/(?P<periodo_id>.+)/', admisiones_views.listar_oferta_periodo, name='listar_oferta_periodo'),
    
    url(r'^periodos/editar-aspirante/(?P<aspirante_id>\d+)/', admisiones_views.editar_aspirante, name='editar_aspirante'),
    
    url(r'^periodos/calcular-admitidos/(?P<periodo_id>.+)/', admisiones_views.calcular_admitidos, name='calcular_admitidos'),
    url(r'^periodos/listar-resultados/(?P<periodo_id>.+)/', admisiones_views.listar_resultados, name='listar_resultados'),
    
    url(r'^pagos/listar-pagos/(?P<periodo_id>.+)/', pagos_views.listar_pagos_periodo, name='listar_pagos_periodo'),
    url(r'^pagos/listar-pagos/', pagos_views.listar_pagos, name='listar_pagos'),
    url(r'^pagos/editar-pago/(?P<pago_id>.+)/', pagos_views.editar_pago, name='editar_pago'),
    
    url(r'^reportes/inscritos-por-periodo/', reportes_views.inscritos_por_periodo, name='inscritos_por_periodo'),
    url(r'^reportes/inscritos-por-oferta/', reportes_views.inscritos_por_oferta, name='inscritos_por_oferta'),
    url(r'^reportes/inscritos-por-fecha-por-periodo/', reportes_views.inscritos_por_fecha_por_periodo, name='inscritos_por_fecha_por_periodo'),
    url(r'^reportes/inscritos-por-programa/', reportes_views.inscritos_por_programa, name='inscritos_por_programa'),
]