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

    def __init__(self, *args, **kwargs):
        super(UserSerializer, self).__init__(*args, **kwargs)
        self.fields["username"].error_messages["required"] = "Por favor, informe o usuário!"
        self.fields["password"].error_messages["required"] = "Por favor, informe a senha!"
        self.fields["email"].error_messages["required"] = "Por favor, informe o e-mail!"
        self.fields["first_name"].error_messages["required"] = "Por favor, informe o primeiro nome!"
        self.fields["last_name"].error_messages["required"] = "Por favor, informe o último nome!"

    # Validação de cadastro -> email duplicado
    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'Este email já foi cadastrado!'})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
