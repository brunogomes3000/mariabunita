from django.contrib import admin
from .models import Usuario
from .models import Tipo_Usuario
from .models import Tipo_Produto
from.models import Produtos
from.models import Compra
from.models import Compra_Produtos

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf']
    search_fields = ['nome', 'cpf']

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Tipo_Usuario)
admin.site.register(Tipo_Produto)
admin.site.register(Pordutos)
admin.site.register(Compra)
admin.site.register(Compra_Produtos)