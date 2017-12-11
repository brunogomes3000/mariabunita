from django.conf.urls import url
from django.contrib import admin
from core import views 
from django.contrib.auth.views import login

urlpatterns = [
	url(r'^$', views.index, name="index"), 
	url(r'^sac/$', views.sac, name="sac"),
	url(r'^visuvendas/$', views.visuvendas, name="visuvendas"), 
	url(r'^visuvendas_detalhes/$', views.visuvendas_detalhes, name="visuvendas_detalhes"),
	url(r'^cadastro/$', views.cadastro,name="cadastro"),
    url(r'^admin/', admin.site.urls),
    url(r'^usuario/$, views.usuario, name="usuario"),
        url(r'^login/$, login {'template_name': 'login.html},
    name="login"), 

]

