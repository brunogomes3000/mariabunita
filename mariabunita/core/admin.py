from django.contrib import admin
from .models import Usuario
from .models import Tipo_Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf']
    search_fields = ['nome', 'cpf']

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Tipo_Usuario)

# Register your models here.