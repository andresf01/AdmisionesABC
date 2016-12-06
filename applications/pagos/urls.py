from django.conf.urls import url

import views

# urls pagos

urlpatterns = [
    url(r'^realizar-pago/(?P<pago_id>\d+)/', views.realizar_pago, name='realizar_pago'),
    url(r'^online$', views.online, name='online')
]