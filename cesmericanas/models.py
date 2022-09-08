from pyexpat import model
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    idade = models.IntegerField()

class Funcionario(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    idade = models.IntegerField()

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)

class Pagamento(models.Model):
    dinheiro = models.CharField(max_length=50)
    cartao = models.CharField(max_length=50)
    pix = models.CharField(max_length=50)

class Ofertas(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
