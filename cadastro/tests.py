from rest_framework import status
from rest_framework.test import APITestCase
from cadastro.models import Cliente

clienteMock = { 'id': 1,'nome': 'Teste', 'cpf': '00000000000' }

class CadastroTests(APITestCase):
  def test_create_client(self):
    response = self.client.post('/clientes/', clienteMock, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Cliente.objects.count(), 1)
    self.assertEqual(Cliente.objects.get().nome, clienteMock['nome'])
    self.assertEqual(Cliente.objects.get().cpf, clienteMock['cpf'])
  
  def test_get_client(self):
    self.client.post('/clientes/', clienteMock, format='json')
    response = self.client.get('/clientes/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data, [clienteMock])
