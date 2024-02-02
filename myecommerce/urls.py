"""myecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from produto.views import home, cad_produto, lista_produtos, produto_detail_view, carrinho, adicionar_ao_carrinho

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('produto/add', cad_produto, name='produto_add'),
    path('produto/lista', lista_produtos, name='produto_lista'),
    path('produto/<slug>', produto_detail_view, name="produto_detalhe"),
    path('carrinho', carrinho, name='produto_carrinho'),
    path('carrinho/add/<int:pk>', adicionar_ao_carrinho, name='carrinho_add'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
