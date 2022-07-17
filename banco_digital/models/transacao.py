import datetime
from django.db import models


class Transacao(models.Model):
    conta_origem = models.CharField(max_length=8, null=False)
    conta_destino = models.CharField(max_length=8, null=False)
    data_transacao = models.DateField(default=datetime.date.today, null=False)
    valor = models.FloatField(null=False)

