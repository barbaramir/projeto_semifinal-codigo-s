from rest_framework import serializers
from banco_digital.models.conta import Conta
from banco_digital.models.transacao import Transacao


class TransacaoSerializer(serializers.HyperlinkedModelSerializer):
       
    class Meta():
        model = Transacao
        fields = "__all__"

    def create(self, validated_data):
        """Determina a transação de valores entre contas."""
        
        conta_origem = Conta.objects.get(conta__exact=validated_data['conta_origem'])
        conta_destino = Conta.objects.get(conta__exact=validated_data['conta_destino'])
        conta_origem.saldo_conta -= validated_data['valor']
        conta_destino.saldo_conta += validated_data['valor']
        conta_origem.save()
        conta_destino.save()
        return super().create(validated_data)    



  

        
