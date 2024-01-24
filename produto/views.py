from django.shortcuts import render

from produto.models import Produto

# Create your views here.

def home(request):
    return render(request, 'home.html')

def cad_produto(request):
    novo_produto = Produto()
    
    novo_usuario.nome = request.POST['nome']
    novo_usuario.idade = request.POST['idade']
    novo_usuario.email = request.POST['email']
    novo_usuario.save()
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    return render(request, 'usuarios.html', usuarios)