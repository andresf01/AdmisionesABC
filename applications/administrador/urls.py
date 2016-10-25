from django.conf.urls import url

import views
import applications.empleados.views as empleados_views
import applications.programas.views as programas_views

# urls administrador

urlpatterns = [
    url(r'^$', views.dashboard, name='administrador'),
    
    url(r'^empleados/crear_empleado/', empleados_views.crear_empleado, name='crear_empleado'),
    url(r'^empleados/editar_empleado/(?P<empleado_id>\d+)/', empleados_views.editar_empleado, name='editar_empleado'),
    url(r'^empleados/setpassword_empleado/(?P<empleado_id>\d+)/', empleados_views.setpassword_empleado, name='setpassword_empleado'),
    url(r'^empleados/ver_empleado/(?P<empleado_id>\d+)/', empleados_views.ver_empleado, name='ver_empleado'),
    url(r'^empleados/listar_empleados/', empleados_views.listar_empleados, name='listar_empleados'),
    
    url(r'^programas/crear_programa/', programas_views.crear_programa, name='crear_programa'),
    url(r'^programas/editar_programa/(?P<programa_id>\d+)/', programas_views.editar_programa, name='editar_programa'),
    url(r'^programas/ver_programa/(?P<programa_id>\d+)/', programas_views.ver_programa, name='ver_programa'),
    url(r'^programas/listar_programas/', programas_views.listar_programas, name='listar_programas'),
    
    # url(r'^periodos/crear-periodo/', periodos_views.crear_periodo, name='crear_periodo'),
    # url(r'^periodos/editar-periodo/(?P<periodo_id>\d+)/', periodos_views.editar_periodo, name='editar_periodo'),
    # url(r'^periodos/ver-periodo/(?P<periodo_id>\d+)/', periodos_views.ver_periodo, name='ver_periodo'),
    # url(r'^periodos/listar-periodos/', periodos_views.listar_periodos, name='listar_periodos'),
]