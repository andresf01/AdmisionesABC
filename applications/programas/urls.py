from django.conf.urls import url

import views

# urls programas

urlpatterns = [
    url(r'^movil/', views.programas_movil, name='programas_movil'),
    url(r'^$', views.programas, name='programas'),
    url(r'^programa/(?P<programa_id>.+)/', views.programa, name='programa')
]