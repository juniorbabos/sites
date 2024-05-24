from django.db import models
from cliente.models import Cliente
from estoque.models import Product

# Create your models here.
class Servico(models.Model):
    servico = models.CharField(verbose_name="Serviço", max_length=150, null=False, blank=False)
    
    #responsavel para mostrar o nome correto no retorno
    def __str__(self):
        return self.servico
    
SITUACAO = (
    ('pe', 'Pendente'),
    ('ca', 'Cancelado'),
    ('an', 'Andamento'),
    ('ap', 'Aprovado'),
)



class OrdemServico(models.Model):
    situacao = models.CharField('Situação', max_length=2, choices=SITUACAO)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.SET_NULL,
        verbose_name='cliente',
        related_name='clientes',
        null=True,
        blank=True
    )
    servico = models.ForeignKey(Servico, 
        on_delete=models.CASCADE,
        null=True,
        blank=True
        )
    produto = models.ForeignKey(Product, 
        on_delete=models.CASCADE,
        null=True,
        blank=True
        )
    #quantidade = models.PositiveIntegerField(verbose_name="quantidade", null=True, blank=True)
    #valor_produto = models.DecimalField('valor Produto', max_digits=10,
    #decimal_places=2, blank=True, default=0)
    valor_custo = models.DecimalField('Valor Custo', max_digits=8, decimal_places=2, null=True, blank=True)
    valor_lucro = models.DecimalField('Valor Lucro', max_digits=8, decimal_places=2, null=True, blank=True)
    data = models.DateField('Data do Serviço', null=True, blank=True)
    observacao = models.TextField('Observacção', null=True, blank=True)
    valor = models.DecimalField('Valor total', max_digits=10,
    decimal_places=2, blank=True, default=0)
    
    def __str__(self):
        return self.servico.servico

    
    #calculo
    def save(self, *args, **kwargs):
    	self.valor_lucro = self.valor - self.valor_custo 
    	self.produto.valor_venda += self.valor_custo
    	self.produto.save()
    	return super(OrdemServico, self).save(*args, **kwargs)
    

       #calculo
   # def save(self, *args, **kwargs):
    #	self.subtotal = self.preco * self.quantidade 
    #	self.compra.valor_compra += self.subtotal
    #	self.compra.save()
    #	return super(Produto, self).save(*args, **kwargs)

    

    


     
    




