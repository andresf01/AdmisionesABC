from django.conf.urls import url

import views

# urls admisiones

urlpatterns = [
    url(r'^$', views.info, name='admisiones'),
    url(r'^inscripcion/', views.inscripcion, name='admisiones_inscripcion'),
    url(r'^aspirante/dashboard/', views.dashboard, name='admisiones_dashboard'),
    url(r'^admitidos/', views.admitidos, name='lista_admitidos'),
    url(r'^calendario/', views.calendario, name='admisiones_calendario'),
]