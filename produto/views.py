from django.shortcuts import redirect, render
from produto.forms import ProdutoForm

from produto.models import Produto
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')

def cad_produto(request):

    print(request.FILES)

    produto = Produto()
    form = ProdutoForm(request.POST, request.FILES, instance=produto)
    if str(request.method) == 'POST':
        if form.is_valid():                 
            print('debug.........')       
            print(form.data)
            form.save()
            messages.success(request, 'Produto cadastrado com sucesso!')
            return redirect('lista_produtos')
        else:
            messages.error(request, 'Erro ao cadastrar o cliente. Contate o administrador')
    return render(request,'cad_produto.html', {'form': form})


def lista_produtos(request):
    lista_produtos = Produto.objects.all().order_by('nome')   
    #paginator = Paginator(clientes_list, 10)
    #page = request.GET.get('page')
    #clientes = paginator.get_page(page)
    context = {
        'lista_produtos' : lista_produtos
	}
    return render(request, 'lista_produtos.html', context)