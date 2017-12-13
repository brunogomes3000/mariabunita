from django.contrib.auth.models import Group
from .models import Usuario

class UsuarioModelForm(forms.ModelForm):	
	class Meta:
		model = Usuario
		fields = ['nome', 'perfil', 'imagem_perfil', 'celular']
			user.save()

			grupo = Group.objects.get(name='Usuarios')
			grupo.user_set.add(user)

			if form2.is_valid():