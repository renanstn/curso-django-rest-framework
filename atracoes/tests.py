import json

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from .api.serializers import AtracoesSerializer
from .api.viewsets import AtracoesViewSet
from .models import Atracao


class AuthTestCase(APITestCase):

    def test_registration(self):
        data = {
            'username': 'testcase',
            'password': 'test123',
        }

        data_atracao = {
            'nome': 'teste',
            'descricao': 'teste',
            'horario_funcionamento': '24h',
            'idade_minima': '10',
        }

        self.user = User.objects.create_user(username="teste", password="teste123")
        self.token = Token.objects.create(user=self.user)

        self.client.credentials(HTTP_AUTHORIZATION="Token "+self.token.key)

        atracoes_url = reverse('atracoes-list')

        response = self.client.get(atracoes_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.post(atracoes_url, data_atracao)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nome'], data_atracao['nome'])
