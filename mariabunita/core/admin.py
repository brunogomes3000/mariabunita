from django.contrib import admin
from .models import Usuario
from .models import Tipo_Usuario
from .models import Tipo_Produto
from.models import Produtos
from.models import Compra
from.models import Compra_Produtos
from.models import Sac

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'imagem_perfil', 'telefone', 'logradouro', 'numero','complemento' , 'usuario', 'senha', 'tipo_usuario']
	search_fields = ['nome', 'cpf', 'imagem_perfil', 'telefone', 'logradouro', 'numero','complemento' , 'usuario', 'senha', 'tipo_usuario']

class Tipo_UsuarioAdmin(admin.ModelAdmin):
	search_fields = ['descricao']

class Tipo_ProdutoAdmin(admin.ModelAdmin):
	search_fields = ['descricao']

class ProdutosAdmin(admin.ModelAdmin)
	list_display = ['nome', 'preco', 'descricao']
	search_fields = ['nome', 'preco', 'descricao']

class Compra(admin.ModelAdmin)
	list_display = ['data_Compra', 'usuario']
	search_fields = ['data_Compra', 'usuario']

class Compra_Produtos(admin.ModelAdmin)
	 list_display = ['qtd', 'compra', 'produtos']
	 search_fields= ['qtd', 'compra', 'produtos']

class Sac(admin.ModelAdmin)
	list_display = ['perguntas', 'resposta']
	search_fields = ['perguntas', 'resposta']



admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Tipo_Usuario)
admin.site.register(Tipo_Produto)
admin.site.register(Produtos)
admin.site.register(Compra)
admin.site.register(Compra_Produtos)
admin.site.register(Sac)
