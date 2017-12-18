from django import forms
from django.forms import ModelForm
from .models import Usuario
from django.contrib.auth.models import Group
			user.save()

			grupo = Group.objects.get(name='Usuarios')
			grupo.user_set.add(user)

			if form2.is_valid():

class UsuarioModelForm(forms.ModelForm):	
	class Meta:
		model = Usuario
		fields = ['cpf','nome','imagem_perfil','telefone','numero', 'logradouro', 'complemento','usuario','senha', 'tipo_usuario','user']
			
			