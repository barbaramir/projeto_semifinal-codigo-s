from rest_framework import viewsets
from banco_digital.models.conta import Conta
from banco_digital.serializers.conta_serializer import ContaSerializer


class ContaViewSet(viewsets.ModelViewSet):
    serializer_class = ContaSerializer
    queryset = Conta.objects.all()