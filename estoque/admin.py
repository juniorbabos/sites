from django.contrib import admin
from .models import Product
from estoque.models import Product, Categoria
from cliente.models import Cliente
from servico.models import Servico, OrdemServico
#from transacao.models import EntradaEstoque, SaidaEstoque

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('codigo_barra','name_product','categoria','estoque_atual','estoque_min','valor_venda','valor_custo')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome','telefone','cpf','endereco','data_criada')

@admin.register(OrdemServico)
class OrdemServicoAdmin(admin.ModelAdmin):
    list_display = ('servico','cliente','situacao','produto','quantidade','valor','data',"valor_custo")

#@admin.register(EntradaEstoque)
#class EntradaEstoqueAdmin(admin.ModelAdmin):
#    list_display = ('produto','quantidade','criado_em')

#@admin.register(SaidaEstoque)
#class SaidaEstoqueAdmin(admin.ModelAdmin):
 #   list_display = ('produto','quantidade','os','cliente','criado_em')

admin.site.register(Categoria)
admin.site.register(Servico)





