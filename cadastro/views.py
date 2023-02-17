from rest_framework import viewsets
from cadastro.models import Cliente
from cadastro.serializer import ClienteSerializer

class ClientesViewSet(viewsets.ModelViewSet):
  queryset = Cliente.objects.all()
  serializer_class = ClienteSerializer
