from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from .models import Sac 
from .models import Compra
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,'index.html')

def contato(request):
    return render (request, 'contato.html')

def sobre(request):
    return render (request, 'sobre.html')

def usuarios(request):
    usuarios = Usuario.objects.all()
    context = {
    'usuarios': usuarios
    }
    return render(request, 'usuarios.html', context)
# Create your views here.


def login (request):
    return render (resquest, 'login.html')


def sac(request):
    sac= Sac.objects.all()
    context = {
    'sac' : sac
    }
    return render(request, 'sac.html', context)

def curso_detalhes(request):
    return render (resquest, 'curso_detalhes.html')


def visuvendas (request):
    vendas=Compra.objects.all()
    context={
        'visuvendas':vendas
    }
    return render (request, 'visuvendas.html', context)

def visuvendas_detalhes(request):
    return render(request, 'visuvendas_detalhes.html')


def cadastro (request):
    return render(request, 'cadastro.html')
    
@login_required(login_url='login')

def usuario(request):
    return render (request, 'usuario.html')

