from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from user.models import User

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=20, min_length=5, write_only=True)
    email = serializers.EmailField(max_length=100, min_length=5)
    first_name = serializers.CharField(max_length=100, min_length=1)
    last_name = serializers.CharField(max_length=100, min_length=1)
    cliente = serializers.BooleanField(default=False, write_only=True)  # Flag para Cliente
    gestor = serializers.BooleanField(default=False, write_only=True)   # Flag para Gestor

    class Meta:
        model = User
        fields=['username', 'first_name', 'last_name', 'email', 'password', 'cliente', 'gestor']

    # Validação de cadastro -> email duplicado
    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'Este email já foi cadastrado!'})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
