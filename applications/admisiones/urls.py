from django.conf.urls import url

import views

# urls admisiones

urlpatterns = [
    url(r'^movil/', views.info_movil, name='admisiones_movil'),
    url(r'^$', views.info, name='admisiones'),
    url(r'^inscripcion/', views.inscripcion, name='admisiones_inscripcion'),
    url(r'^aspirante/dashboard/', views.dashboard, name='admisiones_dashboard'),
    url(r'^admitidos/ajax/', views.resultados_oferta_ajax, name='lista_admitidos_ajax'),
    url(r'^admitidos/movil/', views.resultados_oferta_movil, name='lista_admitidos_movil'),
    url(r'^admitidos/', views.resultados_oferta, name='lista_admitidos'),
    url(r'^calendario/movil/', views.calendario_movil, name='admisiones_calendario_movil'),
    url(r'^calendario/', views.calendario, name='admisiones_calendario'),
]