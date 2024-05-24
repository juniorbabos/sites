from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

#from .forms import OrdemServicoForm
from .models import OrdemServico, Servico


def ordem_servico_list(request):
    template_name = 'servico/ordem_servico_list.html'
    object_list = OrdemServico.objects.all()

    search = request.GET.get('search')
    if search:
        object_list = object_list.filter(situacao=search)

    context = {'object_list': object_list}
    return render(request, template_name, context)


class OrdenServicoCreateView(CreateView):
    model = OrdemServico
    fields = ["servico","cliente","situacao","produto","data","observacao","valor_custo","valor"]
    success_url = reverse_lazy("home")

    



def ordem_servico_detail(request, pk):
    template_name = 'servico/ordem_servico_detail.html'
    instance = OrdemServico.objects.get(pk=pk)
    context = {'object': instance}
    return render(request, template_name, context)


class ServicoCreateView(CreateView):
    model = Servico
    fields = ["servico"]
    success_url = reverse_lazy("home")
