
from django.conf.urls import url
from django.contrib import admin
from core import views 
urlpatterns = [
	url(r'^', views.index, name="index"), 
	url(r'^sac/$', views.sac, name="sac"),
	url(r'^visuvendas/$', views.vendas, name="visuvendas"), 
	url(r'^cadastro/$', views.cadastro,name="cadastro"),
    url(r'^admin/', admin.site.urls),

]

