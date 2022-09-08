from rest_framework import serializers
from .models import Cliente,Funcionario, Ofertas, Pagamento, Produto


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'nome', 'endereco', 'idade')

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ('id', 'nome', 'endereco', 'idade')

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ('id', 'nome', 'tipo','marca')


class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = ('id', 'dinheiro', 'cartao','pix')

class OfertasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ofertas
        fields = ('id', 'nome', 'tipo')
        