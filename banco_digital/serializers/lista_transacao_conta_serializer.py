from rest_framework import serializers
from banco_digital.models.transacao import Transacao


class ListaTransacaoContaSerializer(serializers.ModelSerializer):
    transacao = serializers.ReadOnlyField(source='transacao.data_transacao')
    conta = serializers.ReadOnlyField(source='conta.conta')
    
    class Meta:
        model = Transacao
        fields = [
            'conta_origem'
            'conta_destino',
            'data_transacao',
            'valor',
            ]
            