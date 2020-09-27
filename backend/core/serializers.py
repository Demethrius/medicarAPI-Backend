from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import *

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

    class Meta:
        model = Horario
        fields = ['horario',]


class AgendaSerializer(serializers.ModelSerializer):

    medico = MedicoSerializer(read_only=True)
    horarios = HorarioSerializer(many=True,read_only=True)

    class Meta:
        model = Agenda
        fields = '__all__'


class ConsultaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consulta
        extra_kwargs={
            'data':{'read_only': True},
        }
        exclude = ['user']

