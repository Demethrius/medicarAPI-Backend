from django.shortcuts import render

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from user.serializers import UserSerializer

class CadastrarCliente(GenericAPIView):
    """
    View para cadastro de Cliente
    """

    serializer_class = UserSerializer
    permission_classes=[AllowAny] # Desabilitando autenticação para acessar a rota de signup

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer._validated_data['cliente'] = True    # Set flag de Cliente para True
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CadastrarGestor(GenericAPIView):
    """
    View para cadastro de Gestor
    """

    serializer_class = UserSerializer
    permission_classes=[AllowAny] # Desabilitando autenticação para acessar a rota de signup

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer._validated_data['gestor'] = True     # Set flag de Gestor para True
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
