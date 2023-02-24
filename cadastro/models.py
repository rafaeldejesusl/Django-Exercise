from django.db import models
from datetime import date


class Cliente(models.Model):
    nome = models.CharField(max_length=40)
    cpf = models.CharField(max_length=11, unique=True)
    data_de_nascimento = models.DateField(default=date.min)
    email = models.EmailField(
        max_length=40,
        default="example@email.com",
        unique=True
    )

    def __str__(self) -> str:
        return self.nome
