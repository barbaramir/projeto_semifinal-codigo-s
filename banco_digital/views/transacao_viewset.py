from rest_framework import viewsets
from banco_digital.models.transacao import Transacao
from banco_digital.serializers.transacao_serializer import TransacaoSerializer



class TransacaoViewSet(viewsets.ModelViewSet):
    serializer_class = TransacaoSerializer
    queryset = Transacao.objects.all()