from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import *


class AgendaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agenda
        fields = '__all__'


class EspecialidadeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Especialidade
        fields = ['id', 'nome',]


class MedicoSerializer(serializers.ModelSerializer):

    especialidade = EspecialidadeSerializer(read_only=True)

    class Meta:
        model = Medico
        fields = ['nome', 'crm', 'email', 'telefone', 'especialidade',]


class HorarioSerializer(serializers.ModelSerializer):

    hora = AgendaSerializer(many=True, read_only=True)

    class Meta:
        model = Horario
        fields = ['horario',]


class ConsultaSerializer(serializers.ModelSerializer):

    medico = MedicoSerializer(read_only=True)

    class Meta:
        model = Consulta
        fields = '__all__'

