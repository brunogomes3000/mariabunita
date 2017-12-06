from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from .models import Sac 
from .models import Compra


def index(request):
    sac= Sac.objects.all().order_by ('-id')[:3] 
    return render(request,'index.html')
    context = {
    'sac': sac
    }

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


def login (resquest):
	return render (resquest, 'login.html')


def sac( resquest):
	sac= Sac.objects.all()
	context = {
	'sac' : sac
	}
	return render(requesr, 'sac.html', context)

def Compras (request):
	vendas=Compras.objects.all()
	context={
        'visuvendas':vendas
    }
	return render (request, 'visuvendas.html', context)

def visuvendas_detalhes(request):
    return render(request, 'visuvendas_detalhes.html')


def cadastro (request):
    return render(request, 'cadastro.html')

