from django.conf.urls import url

import views

# urls admisiones

urlpatterns = [
    url(r'^$', views.info, name='admisiones'),
    url(r'^inscripcion/', views.inscripcion, name='admisiones_inscripcion'),
    url(r'^info/', views.info, name='admisiones_informacion'),
    url(r'^aspirante/dashboard', views.dashboard, name='admisiones_dashboard'),
]