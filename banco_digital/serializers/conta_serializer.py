from rest_framework import serializers
from banco_digital.models.conta import Conta


class ContaSerializer(serializers.HyperlinkedModelSerializer):
    banco = serializers.CharField(max_length=4, default='0001', read_only=True)

    def create(self, validated_data):
        validated_data['saldo_conta'] = validated_data['deposito_inicial']
        return super().create(validated_data)

    class Meta():
        model = Conta
        fields = [
            'cliente',
            'banco',
            'agencia',
            'conta',
            'data_abertura',
            'deposito_inicial',
            'saldo_conta'
        ]
        read_only_fields = ['banco', 'data_abertura', 'saldo_conta']
        