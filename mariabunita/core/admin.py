from django.contrib import admin
from .models import Usuario
from .models import Tipo_Usuario
from .models import Tipo_Produto
from.models import Produtos
from.models import Compra
from.models import Compra_Produtos
from.models import Sac

class UsuarioAdmin(admin.ModelAdmin):
	list_display = ['nome','cpf']
	search_fields = ['nome','cpf']
    
class Tipo_UsuarioAdmin(admin.ModelAdmin):
	search_fields = ['descricao']

class Tipo_ProdutoAdmin(admin.ModelAdmin):
	search_fields = ['descricao']
	lister_filter = ['lábios' , 'face', 'olhos' , 'picel']
class ProdutosAdmin(admin.ModelAdmin):
	list_display = ['nome', 'preco', 'descri']
	search_fields = ['nome', 'preco', 'descri']

class CompraAdmin(admin.ModelAdmin):
	list_display = ['data_Compra', 'usuario']
	search_fields = ['data_Compra', 'usuario']

class Compra_ProdutosAdmin(admin.ModelAdmin):
	list_display = ['qtd', 'compra', 'produtos']
	search_fields= ['qtd', 'compra', 'produtos']

class SacAdmin(admin.ModelAdmin):
	list_display = ['perguntas', 'resposta']
	search_fields = ['perguntas', 'resposta']



admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Tipo_Usuario, Tipo_UsuarioAdmin)
admin.site.register(Tipo_Produto, Tipo_ProdutoAdmin)
admin.site.register(Produtos, ProdutosAdmin)
admin.site.register(Compra, CompraAdmin)
admin.site.register(Compra_Produtos, Compra_ProdutosAdmin)
admin.site.register(Sac, SacAdmin)
