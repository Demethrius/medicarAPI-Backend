from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from core.models import *
from core.serializers import *

class EspecialidadeCreate(generics.ListAPIView):

    serializer_class = EspecialidadeSerializer
    permission_classes=[IsAuthenticated]

    #Filtragem por nome da especialidade
    def get_queryset(self):
        queryset = Especialidade.objects.all()

        nome = self.request.query_params.get('search', None)
        if nome is not None:
            queryset = Especialidade.objects.filter(nome=nome)
            return queryset
        
        return queryset


class MedicoCreate(generics.ListAPIView):

    serializer_class = MedicoSerializer
    permission_classes=[IsAuthenticated]

    #Filtragem por nome da especialidade e nome do médico
    def get_queryset(self):
        queryset = Medico.objects.all()

        nome = self.request.query_params.get('search', None)
        especialidade = self.request.query_params.get('especialidade', None)

        if nome is not None:
            queryset = Medico.objects.filter(nome=nome)
            return queryset

        if especialidade is not None:
            queryset = Medico.objects.filter(especialidade__nome=especialidade)
            return queryset

        return queryset


class HorarioCreate(generics.ListAPIView):

    serializer_class = HorarioSerializer
    permission_classes=[IsAuthenticated]
    queryset = Horario.objects.all()


class AgendaCreate(generics.ListAPIView):

    serializer_class = AgendaSerializer
    permission_classes=[IsAuthenticated]

    #Filtragem por nome da especialidade e nome do médico e intervalo de datas
    def get_queryset(self):
        queryset = Agenda.objects.exclude(dia__lt=datetime.date.today()) # Não exibir datas passadas

        nome = self.request.query_params.get('search', None)
        especialidade = self.request.query_params.get('especialidade', None)
        data_inicio = self.request.query_params.get('data_inicio', None)
        data_final = self.request.query_params.get('data_final', None)

        if nome is not None:
            queryset = Agenda.objects.filter(medico__nome=nome)
            return queryset

        if especialidade is not None:
            queryset = Agenda.objects.filter(medico__especialidade__nome=especialidade)
            return queryset

        if data_final and data_inicio is not None:
            queryset = Agenda.objects.filter(dia__gte=data_inicio, dia__lte=data_final)
            return queryset

        return queryset


class ConsultaCreate(generics.ListAPIView):

    serializer_class = ConsultaSerializer
    permission_classes=[IsAuthenticated]

    # Filtragem não exibe datas de consultas anteriores ao dia atual
    def get_queryset(self):
        queryset=Consulta.objects.filter(user=self.request.user).exclude(data__lt=datetime.date.today())
        return queryset
