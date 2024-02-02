from django.shortcuts import get_object_or_404, redirect, render
from produto.forms import ProdutoForm

from produto.models import Produto
from django.contrib import messages

# Create your views here.

def home(request):
          
    lista_produtos = Produto.objects.all().order_by('nome')   
    #paginator = Paginator(clientes_list, 10)
    #page = request.GET.get('page')
    #clientes = paginator.get_page(page)
    context = {
        'lista_produtos' : lista_produtos
	}    
    return render(request, 'home.html', context)

def cad_produto(request):

    produto = Produto()
    form = ProdutoForm(request.POST, request.FILES, instance=produto)
    if str(request.method) == 'POST':
        if form.is_valid():              
            form.save()
            messages.success(request, 'Produto cadastrado com sucesso!')
            return redirect('lista_produtos')
        else:
            messages.error(request, 'Erro ao cadastrar o cliente. Contate o administrador')
    return render(request,'cad_produto.html', {'form': form})


def lista_produtos(request):
    produtos = Produto.objects.all().order_by('nome')   
    #paginator = Paginator(clientes_list, 10)
    #page = request.GET.get('page')
    #clientes = paginator.get_page(page)
    
    return render(request, 'lista_produtos.html', context= {'lista_produtos' : produtos })


def produto_detail_view(request, slug):
    produto = get_object_or_404(Produto, slug=slug)
    print(produto)
    return render(request, 'produto_detalhe.html', context={'produto': produto})

def carrinho(request):
    if not request.session.get('carrinho'):
        request.session['carrinho'] = {}
        request.session.save()
    if not request.session.get('total'):
        request.session['total'] = 0
        request.session.save()
    context={'carrinho': request.session['carrinho'], 'total':request.session['total']}
    return render(request, 'carrinho.html', context)

def adicionar_ao_carrinho(request, pk):
    
    if not request.session.get('carrinho'):
        request.session['carrinho'] = {}
        request.session.save()

    carrinho = request.session['carrinho']
    
    produto = get_object_or_404(Produto, pk=pk)
    pk = str(pk)
    if pk in carrinho:
        print('if...........')
        quantidade_carrinho = carrinho[pk]['quantidade']
        quantidade_carrinho += 1

        carrinho[pk]['quantidade'] = quantidade_carrinho
        carrinho[pk]['preco_quantitativo'] = produto.preco_marketing * quantidade_carrinho
        carrinho[pk]['preco_quantitativo_promocional'] = produto.preco_marketing_promocional * quantidade_carrinho
    else:
        print('else.........')
        print(pk)
        print(carrinho)
        carrinho[pk] = {
            'produto_id': produto.id,
            'produto_nome': produto.nome,
            'preco_unitario': produto.preco_marketing ,
            'preco_unitario_promocional': produto.preco_marketing_promocional ,
            'preco_quantitativo': produto.preco_marketing,
            'preco_quantitativo_promocional': produto.preco_marketing_promocional ,
            'quantidade': 1,
            'slug': produto.slug,
            'imagem': produto.imagem.name,
        }
    
    total = 0
    for p in carrinho:
        p = carrinho[p]
        total += p['quantidade']
    request.session['total'] = total
    request.session.save()

    messages.success(
        request,
        f'Produto {produto.nome} adicionado ao seu '
        f'carrinho {carrinho[pk]["quantidade"]}x.'
    )

    return redirect('produto_carrinho')