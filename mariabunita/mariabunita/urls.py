
from django.conf.urls import url
from django.contrib import admin
from core import views 
urlpatterns = [

	url (r'^sac/$', views.sac, name="sac"), 

	url(r'cadastro/$', views.cadastro,name="cadastro"),

    url(r'^admin/', admin.site.urls),

]

