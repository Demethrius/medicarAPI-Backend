import json

from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from user.serializers import UserSerializer
from user.models import User

class ListaEspecialidadesTestCase(APITestCase):
    """
    Teste de listagem dos Especialidades
    """
    url = reverse('especialidades')

    # Criação do usuário para fazer login e receber o JWT no endpoint de authorization
    def setUp(self):
        self.user = User.objects.create_user(username="testCase1", password="case@@123!@#")

    def test_list_especialidades(self):

        data = {
            "username":"testCase1",
            "password":"case@@123!@#"
        }

        # Teste de login e receber o token JWT de volta
        response = self.client.post('/api/token', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data['token']

        # Teste da rota de listagem dos especialidades passando o JWT INVÁLIDO no Header da requisição
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + 'token')
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

        # Teste da rota de listagem dos especialidades passando o JWT VÁLIDO no Header da requisição
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

class ListaMedicosTestCase(APITestCase):
    """
    Teste de listagem dos Médicos
    """
    url = reverse('medicos')

    # Criação do usuário para fazer login e receber o JWT no endpoint de authorization
    def setUp(self):
        self.user = User.objects.create_user(username="testCase1", password="case@@123!@#")

    def test_list_medicos(self):

        data = {
            "username":"testCase1",
            "password":"case@@123!@#"
        }

        # Teste de login e receber o token JWT de volta
        response = self.client.post('/api/token', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data['token']

        # Teste da rota de listagem dos medicos passando o JWT INVÁLIDO no Header da requisição
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + 'token')
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

        # Teste da rota de listagem dos medicos passando o JWT VÁLIDO no Header da requisição
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)



class ListaHorariosTestCase(APITestCase):
    """
    Teste de listagem dos Horários
    """
    url = reverse('horarios')

    # Criação do usuário para fazer login e receber o JWT no endpoint de authorization
    def setUp(self):
        self.user = User.objects.create_user(username="testCase1", password="case@@123!@#")

    def test_list_horarios(self):

        data = {
            "username":"testCase1",
            "password":"case@@123!@#"
        }

        # Teste de login e receber o token JWT de volta
        response = self.client.post('/api/token', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data['token']

        # Teste da rota de listagem dos horarios passando o JWT INVÁLIDO no Header da requisição
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + 'token')
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

        # Teste da rota de listagem dos horarios passando o JWT VÁLIDO no Header da requisição
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class ListaAgendasTestCase(APITestCase):
    """
    Teste de listagem das Agendas
    """
    url = reverse('agendas')

    # Criação do usuário para fazer login e receber o JWT no endpoint de authorization
    def setUp(self):
        self.user = User.objects.create_user(username="testCase1", password="case@@123!@#")

    def test_list_agendas(self):

        data = {
            "username":"testCase1",
            "password":"case@@123!@#"
        }

        # Teste de login e receber o token JWT de volta
        response = self.client.post('/api/token', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data['token']

        # Teste da rota de listagem das agendas passando o JWT INVÁLIDO no Header da requisição
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + 'token')
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

        # Teste da rota de listagem das agendas passando o JWT VÁLIDO no Header da requisição
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)



class ListaConsultasTestCase(APITestCase):
    """
    Teste de listagem das Consultas
    """
    url = reverse('consultas')

    # Criação do usuário para fazer login e receber o JWT no endpoint de authorization
    def setUp(self):
        self.user = User.objects.create_user(username="testCase1", password="case@@123!@#")

    def test_list_consultas(self):

        data = {
            "username":"testCase1",
            "password":"case@@123!@#"
        }

        # Teste de login e receber o token JWT de volta
        response = self.client.post('/api/token', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data['token']

        # Teste da rota de listagem das consultas passando o JWT INVÁLIDO no Header da requisição
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + 'token')
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

        # Teste da rota de listagem das consultas passando o JWT VÁLIDO no Header da requisição
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
