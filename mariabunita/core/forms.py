from django import forms
from django.forms import ModelForm
from .models import Usuario

class UsuarioModelForm(forms.ModelForm):	
	class Meta:
		model = Usuario
		fields = ['cpf','nome','imagem_perfil','telefone','numero', 'logradouro', 'complemento','usuario','senha', 'tipo_usuario','user']
			
			