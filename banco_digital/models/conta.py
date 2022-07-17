import datetime
from django.db import models
from banco_digital.models.cliente import Cliente


class Conta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    banco = models.CharField(max_length=4, default='0001')
    agencia = models.CharField(max_length=4)
    conta = models.CharField(max_length=8, unique=True)
    data_abertura = models.DateField(default=datetime.date.today, null=False)
    deposito_inicial = models.FloatField(null=True, default=0.00)
    saldo_conta = models.FloatField(null=True, default=0.00)

    def __str__(self) -> str:
        return self.conta
