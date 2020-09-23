from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import *


class AgendaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agenda
        fields = '__all__'


class ConsultaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consulta
        fields = '__all__'


class EspecialidadeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Especialidade
        fields = ['id', 'nome',]


class MedicoSerializer(serializers.ModelSerializer):

    agenda = AgendaSerializer(many=True, read_only=True)
    consultas = ConsultaSerializer(many=True, read_only=True)
    especialidade = EspecialidadeSerializer(read_only=True)

    class Meta:
        model = Medico
        fields = ['nome', 'crm', 'email', 'telefone', 'especialidade', 'consultas', 'agenda']


class HorarioSerializer(serializers.ModelSerializer):

    hora = AgendaSerializer(many=True, read_only=True)

    class Meta:
        model = Horario
        fields = ['horario',]


