from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from.models import Sac 

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


def login (resquest):
	return render (resquest, 'login.html')

def sac( resquest):
	sac= Curso.objects.all()
	context = {
	'sac' : sac
	}
	return render(requesr, 'sac.html', context)
