from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from .models import Sac 
from .models import Compra
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import UsuarioModelForm
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from . models import Produtos

def index(request):
    return render(request,'index.html')

def contato(request):
    return render (request, 'contato.html')

def sobre(request):
    return render (request, 'sobre.html')

@login_required(login_url='login')
def usuarios(request):
    usuarios = Usuario.objects.all()
    context = {
    'usuarios': usuarios
    }
    return render(request, 'usuario.html', context)
# Create your views here.


def login (request):
    return render (resquest, 'login.html')


def sac(request):
    sac= Sac.objects.all()
    context = {
    'sac' : sac
    }
    return render(request, 'sac.html', context)



def visuvendas (request):
    vendas=Compra.objects.all()
    context={
        'visuvendas':vendas
    }
    return render (request, 'visuvendas.html', context)

def visuvendas_detalhes(request):
    return render(request, 'visuvendas_detalhes.html')


def cadastro(request):
    form = UserCreationForm(request.POST or None)
    form2 = UsuarioModelForm(request.POST or None)
    context = {
        'form': form,
        'form2': form2
    }
    if request.method == 'POST':
        if form.is_valid():
            user_post = UserCreationForm(request.POST)
            user = user_post.save(commit=False)
            user.set_password(user_post.cleaned_data['password1'])
            user.save()

            if form2.is_valid():
                usuario_post = UsuarioModelForm(request.POST)
                usuario = usuario_post.save(commit=False)
                usuario.user = user
                usuario.save()                                                                           

            return redirect('/sucesso')
    return render(request, 'cadastro.html', context)


@login_required(login_url='login')
def usuario(request):
    return render (request, 'usuario.html')


def sucesso(request):
    return render(request, 'sucesso.html')

def Produtos (request) :
    Produtos = Produtos.objects.all()
    context = {
    'produtos': produtos

    }
    return render (request, "produtos.html", context)
