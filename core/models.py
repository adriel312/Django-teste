from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField('Nome',max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Estoque')

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField()
    cpf = models.IntegerField()

    def __str__(self):
        return self.nome