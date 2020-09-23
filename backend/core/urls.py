from django.urls import path
from core.views import *

urlpatterns = [

    path('especialidades/', EspecialidadeCreate.as_view(), name="especialidades"),
    path('medicos/', MedicoCreate.as_view(), name="medicos"),
    path('horarios/', HorarioCreate.as_view(), name="horarios"),
    path('agenda/', AgendaCreate.as_view(), name="agenda"),
    path('consultas/', ConsultaCreate.as_view(), name="consultas"),

]
