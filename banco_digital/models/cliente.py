from django.db import models


class Cliente(models.Model):
    PESSOA_FISICA = 'PF'
    PESSOA_JURIDICA = 'PJ'

    TIPO_PESSOA = [
        (PESSOA_FISICA, 'fisica'),
        (PESSOA_JURIDICA, 'juridica'),
    ]
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, null=True)
    cnpj = models.CharField(max_length=14, null=True)
    telefone = models.CharField(max_length=11)
    email = models.CharField(max_length=45)
    endereco = models.CharField(max_length=100)
    tipo = models.CharField(max_length=2, choices=TIPO_PESSOA, default=PESSOA_FISICA)

    def __str__(self) -> str:
        return self.nome
