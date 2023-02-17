from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=40)
    cpf = models.CharField(max_length=11)

    def __str__(self) -> str:
        return self.nome
