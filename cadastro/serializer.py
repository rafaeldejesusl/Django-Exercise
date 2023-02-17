from rest_framework import serializers
from cadastro.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cliente
    Fields = ['id', 'nome', 'cpf']
