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
    queryset = Medico.objects.all()


class HorarioCreate(generics.ListAPIView):

    serializer_class = HorarioSerializer
    permission_classes=[IsAuthenticated]
    queryset = Horario.objects.all()


class AgendaCreate(generics.ListAPIView):

    serializer_class = AgendaSerializer
    permission_classes=[IsAuthenticated]
    queryset = Agenda.objects.all()


class ConsultaCreate(generics.ListAPIView):

    serializer_class = ConsultaSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        queryset=Consulta.objects.filter(user=self.request.user)
        return queryset
