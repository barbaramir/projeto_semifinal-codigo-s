from rest_framework import generics
from banco_digital.models.transacao import Transacao
from banco_digital.serializers.lista_transacao_conta_serializer import ListaTransacaoContaSerializer


class ListaTransacaoContaViewset(generics.ListAPIView):
    """Listando as transações de uma conta"""

    def get_queryset(self):
        queryset = Transacao.objects.filter(conta_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaTransacaoContaSerializer