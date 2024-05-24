
from django.contrib import admin
from django.urls import path,include
from estoque import views as v
from cliente import views as c
from servico import views as s
from transacao import views as t
from cliente.views import ClientListView, ClientCreateView, ClientDeleteView, ClientUpdateView
from estoque.views import ProdutoList, ProdutoCreateView, CategoriaCreateView       
from transacao.views import orcamento,TransacaoListView,transacao_detail, TransacaoDeleteView, FornecedorCreateView, FornecedorListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('estoque/', v.ProdutoList.as_view(), name="home_estoque"),
    path ('estoque/cadastro', v.ProdutoCreateView.as_view(), name="cadastrar_produto"),
    path('atualiza_produto/<int:pk>', v.ProductUpdateView.as_view(), name="atualiza_produto"),
    path('delete/<int:pk>',v.ProductDeleteView.as_view(), name="delete_produto"),
    path ('estoque/cadastro_categoria', v.CategoriaCreateView.as_view(), name="cadastro_categoria"),
    path ('estoque/listar_categoria', v.CategoriaListView.as_view(), name="listar_categoria"),
    path('', v.home, name="home"),

    #URLS dos clientes
    path('cliente/', c.ClientListView.as_view(), name="clientes"),
    path ('cadastrar_cliente', c.ClientCreateView.as_view(), name="cadastrar_cliente"),
    path('atualiza_cliente/<int:pk>', c.ClientUpdateView.as_view(), name="atualiza_cliente"),
    path('delete_cliente/<int:pk>', c.ClientDeleteView.as_view(), name="delete_cliente"),

    #URLS dos serviços
      path('servico/', s.ordem_servico_list, name='home_servicos'),  # noqa E501
      path('servico/cadastrar_ordemservico', s.OrdenServicoCreateView.as_view(), name='ordem_servico_create'),  # criacao do serviço
      path('visualizar_os/<int:pk>', s.ordem_servico_detail, name="visualizar_os"),
      path('servico/criar', s.ServicoCreateView.as_view(), name="cadastrar_servico"),

    #URLS ORÇAMENTO
    path('orcamento/<int:id>/', t.orcamento, name='orcamento'),
    path('transacao/listar_orcamentos/', t.TransacaoListView.as_view(), name='listar_orcamento'),
    path('trasancao/<int:id>/', t.transacao_detail, name='visualizar_orcamento'),
    path('delete_orcamento/<int:pk>', t.TransacaoDeleteView.as_view(), name="delete_orcamento"),

    #URL FORNECEDOR
    path('cadastro_fornecedor', t.FornecedorCreateView.as_view(), name='cadastrar_fornecedor'),
    path('visualizar_fornecedor', t.FornecedorListView.as_view(), name='listar_fornecedor'),
]
