from django.conf.urls import url
from django.contrib import admin
from core import views 
from django.contrib.auth.views import login
from django.contrib.auth.views import logout 


urlpatterns = [
	url(r'^$', views.index, name="index"), 
	url(r'^sac/$', views.sac, name="sac"),
	url(r'^visuvendas/$', views.visuvendas, name="visuvendas"), 
	url(r'^visuvendas_detalhes/$', views.visuvendas_detalhes, name="visuvendas_detalhes"),
	url(r'^cadastro/$', views.cadastro,name="cadastro"),
	url(r'^sucesso/$', views.sucesso,name="sucesso"),
	url(r'^usuarios/$', views.usuarios, name="usuarios"),
	url(r'^login/$', login, {'template_name': 'login.html'}, name="login"),
	url(r'^sair/$', logout, {'next_page': '/'}, name="logout"),
	url(r'^produtos/$', views.produtos, name="produtos"),
	url(r'^detalhes_produtos/$', views.detalhes_produtos, name="detalhes_produtos"),
	url(r'^admin/', admin.site.urls)
	]
