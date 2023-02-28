from rest_framework import status
from rest_framework.test import APITestCase
from cadastro.models import Cliente
from datetime import date

clienteMock = {
    'id': 1,
    'nome': 'Teste',
    'cpf': '00000000000',
    'data_de_nascimento': '2004-06-24',
    'email': 'teste@email.com'
}

updateMock = {
    'id': 1,
    'nome': 'Updated',
    'cpf': '99999999999',
    'data_de_nascimento': '2004-06-25',
    'email': 'updated@email.com'
}


class CadastroTests(APITestCase):
    def test_create_client(self):
        response = self.client.post('/clientes/', clienteMock, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cliente.objects.count(), 1)
        self.assertEqual(Cliente.objects.get().nome, clienteMock['nome'])
        self.assertEqual(Cliente.objects.get().cpf, clienteMock['cpf'])
        self.assertEqual(
            Cliente.objects.get().data_de_nascimento,
            date(2004, 6, 24)
        )
        self.assertEqual(Cliente.objects.get().email, clienteMock['email'])

    def test_get_client(self):
        self.client.post('/clientes/', clienteMock, format='json')
        response = self.client.get('/clientes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [clienteMock])

    def test_get_by_id_client(self):
        self.client.post('/clientes/', clienteMock, format='json')
        response = self.client.get('/clientes/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, clienteMock)

    def test_update_client(self):
        self.client.post('/clientes/', clienteMock, format='json')
        response = self.client.put('/clientes/1/', updateMock, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Cliente.objects.count(), 1)
        self.assertEqual(Cliente.objects.get().nome, updateMock['nome'])
        self.assertEqual(Cliente.objects.get().cpf, updateMock['cpf'])
        self.assertEqual(
            Cliente.objects.get().data_de_nascimento,
            date(2004, 6, 25)
        )
        self.assertEqual(Cliente.objects.get().email, updateMock['email'])

    def test_delete_client(self):
        self.client.post('/clientes/', clienteMock, format='json')
        response = self.client.delete('/clientes/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Cliente.objects.count(), 0)

    def test_error_no_name(self):
        response = self.client.post(
            '/clientes/',
            {
                'cpf': clienteMock['cpf'],
                'data_de_nascimento': clienteMock['data_de_nascimento'],
                'email': clienteMock['email']
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Cliente.objects.count(), 0)

    def test_error_no_cpf(self):
        response = self.client.post(
            '/clientes/',
            {
                'nome': clienteMock['nome'],
                'data_de_nascimento': clienteMock['data_de_nascimento'],
                'email': clienteMock['email']
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Cliente.objects.count(), 0)
