#declarando models
from django.db import models
from django.urls import reverse_lazy

class Product(models.Model):

    name_product = models.CharField(verbose_name="Produto", max_length=150, null=False, blank=False)
    descricao = models.CharField(max_length=250, null=True)
    codigo_barra = models.CharField(max_length=50, null=True)
    estoque_min = models.IntegerField(null=True)
    estoque_atual = models.IntegerField(null=True)
    valor_custo = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    valor_venda = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    categoria = models.ForeignKey(
        'Categoria',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('name_product',)

    def __str__(self):
        return self.name_product
    def get_absolute_url(self):
        return reverse_lazy('product_name:produto_detail', kwargs={'pk': self.pk})

    def to_dict_json(self):
        return {
            'pk': self.pk,
            'product_name': self.name_product,
            'estoque_atual': self.estoque_atual,
        }


class Categoria(models.Model):
    categoria = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('categoria',)

    def __str__(self):
        return self.categoria

