from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Product, Categoria

from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin as LRM


class SearchMixin:
    # buscar 
    def get_queryset(self):
        queryset = super(SearchMixin, self).get_queryset()
        buscar = self.request.GET.get('buscar')
        if buscar:
            return queryset.filter(
                Q(name_product__icontains=buscar) |
                Q(codigo_barra__icontains=buscar) |
                Q(descricao__icontains=buscar)
            )
        return queryset
    # fim buscar 


#class para listar os produtos em formado de tabelas ordenadas
class ProdutoList(LRM, SearchMixin, ListView):
    model = Product
    template_name = 'product_list.html'
    paginate_by = 10


#class para criarmos novos produtos 
class ProdutoCreateView(CreateView):
    model = Product
    fields = ["name_product","categoria","descricao","codigo_barra","estoque_min","estoque_atual","valor_custo","valor_venda"]
    success_url = reverse_lazy("home_estoque")

#class para fazer alterações no produto
class ProductUpdateView(UpdateView,ListView):
    model = Product
    fields = ["name_product","categoria","descricao","codigo_barra","estoque_min","estoque_atual","valor_custo","valor_venda"]
    success_url = reverse_lazy("home_estoque")

#c class para realizar o delete do produto
class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("home_estoque")

#class para cadastrar Categoria 
class CategoriaCreateView(CreateView):
    model = Categoria
    fields = ['categoria']
    success_url = reverse_lazy("cadastrar_produto")

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria_list.html'
    paginate_by = 10

#class home para listar 
def home(request):
    context = {
        "home": home,
    }
    return render(request, "index.html", context)

