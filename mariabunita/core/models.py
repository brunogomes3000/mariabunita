from django.db import models
from django.contrib.auth.models import User

class Tipo_Usuario(models.Model):
    descricao = models.CharField('Descrição', max_length=100)
   
    def __str__(self):
        return self.descricao

class Usuario(models.Model):
    cpf = models.CharField('CPF', primary_key=True, max_length=11)
    nome = models.CharField('Nome', max_length=100)
    imagem_perfil = models.ImageField( upload_to='imagens/perfil', verbose_name='Imagem', default='imagens/perfil/noperfil.png', null=True, blank=True)
    telefone = models.CharField('Telefone', max_length=14)
    logradouro = models.CharField('Logradouro', max_length=200)
    numero = models.CharField('Número', max_length=50)
    complemento = models.CharField('Complemento', max_length=200)
    tipo_usuario = models.ForeignKey(Tipo_Usuario, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['-nome']


class Tipo_Produto(models.Model):
    descricao = models.CharField('Descrição', max_length=100)

    def __str__(self):
        return self.descricao

class Produtos(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    descri = models.CharField('Descrição', max_length=100)
    tipo_produto = models.ForeignKey(Tipo_Produto, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class Compra(models.Model):
    data_Compra = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario , on_delete=models.CASCADE)
def __str__(self):
        return self.data_Compra
   
class Compra_Produtos(models.Model):
    qtd = models.CharField('Quantidade', max_length=100)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    produtos = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    def __str__(self):
        return self.produtos
    
class Sac(models.Model):
    perguntas=models.CharField('Perguntas', max_length=500)
    resposta= models.CharField('Resposta', max_length=4000)

    def __str__(self):
        return self.perguntas

    class Meta:
        verbose_name='Sac'
        verbose_name_plural= 'Sac'


