from rest_framework import serializers
from banco_digital.models.conta import Conta


class ListaContaClienteSerializer(serializers.ModelSerializer):
    conta = serializers.ReadOnlyField(source='conta.conta')
    cliente = serializers.ReadOnlyField(source='cliente.nome')
    
    class Meta:
        model = Conta
        fields = [
            'cliente',
            'banco',
            'agencia',
            'conta',
            'saldo_conta',
            ]
            