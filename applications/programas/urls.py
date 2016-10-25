from django.conf.urls import url

import views

# urls programas

urlpatterns = [
    url(r'^$', views.programas, name='programas'),
    url(r'^programa/(?P<programa_id>.+)/', views.programa, name='programa')
]