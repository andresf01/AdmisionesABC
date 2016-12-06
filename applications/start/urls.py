from django.conf.urls import url
import django.contrib.auth.views

from forms import LoginForm
import views

# urls start

urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^login$', django.contrib.auth.views.login, {'template_name':'init/login.html', 'authentication_form':LoginForm}, name='login'),
    url(r'^login$', views.custom_login, name='login'),
    url(r'^logout$', django.contrib.auth.views.logout, {'next_page':'/'}, name='logout'),
    url(r'^dashboard$', views.redirect_to_dashboard, name='dashboard'),
]