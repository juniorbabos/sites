# -*- Mode: Python; coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView
from .models import Fornecedor, Compra, Produto, Material



@login_required(redirect_field_name='redirect_to')
def orcamento(request, id=None, *args, **kwargs):
	contexto = {}
	contexto['orcamento'] = Compra.objects.get(id=id)

	return render(request, "orcamento.html", contexto)


#class  base de views utilizando a class Clients
class TransacaoListView(ListView):
    model = Compra
    template_name = 'transacao_list.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def transacao_detail(request, pk):
    template_name = 'transacao/orcamento_detail.html'
    instance = Compra.objects.get(pk=pk)
    context = {'object': instance}
    return render(request, template_name, context)


