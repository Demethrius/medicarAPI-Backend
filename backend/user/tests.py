import json

from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from user.serializers import UserSerializer
from user.models import User

class RegistrationTestCase(APITestCase):
    """
    Teste da função de cadastro de usuário
    """

    def test_registration(self):

        data = {
            "username":"testCase1",
            "password":"testCase1",
            "email":"testCase1@testCase1.com.br",
            "first_name": "Test",
            "last_name": "Case"
        }

        response = self.client.post('/api/auth/cadastrar_cliente/', data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class AuthenticationTestCase(APITestCase):
    """
    Teste de login
    """

    def setUp(self):
        self.user = User.objects.create_user(username="test", password="case@123!@#")

    def test_authentication(self):

        data = {
            "username":"test",
            "password":"case@123!@#"
        }

        response = self.client.post('/api/token', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
