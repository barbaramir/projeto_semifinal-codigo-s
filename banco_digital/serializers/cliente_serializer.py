from rest_framework import serializers
from banco_digital.models.cliente import Cliente


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    cpf = serializers.CharField(required=False)
    cnpj = serializers.CharField(required=False)
    telefone = serializers.CharField(min_length=10)

    class Meta():
        model = Cliente
        fields = "__all__"

    def validate(self, data):
        """Valida os campos CPF e CNPJ inseridos."""
        
        if (data.get("tipo") == 'PJ'):
            if data.get("cnpj") == None:
                raise serializers.ValidationError('CNPJ é um campo obrigatório!')
            elif len(data.get("cnpj")) != 14:
                raise serializers.ValidationError('CNPJ deve conter 14 números.')
            return data

        elif (data.get("tipo") == 'PF'):
            if data.get("cpf") == None:
                raise serializers.ValidationError('CPF é um campo obrigatório!')
            elif len(data.get("cpf")) != 11:
                raise serializers.ValidationError('CPF deve conter 11 números.')
            return data
  