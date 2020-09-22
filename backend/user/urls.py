from django.urls import path

from user.views import CadastrarCliente, CadastrarGestor

urlpatterns = [
    path('cadastrar_cliente/', CadastrarCliente.as_view(), name="cadastrar_cliente"),
    path('cadastrar_gestor/', CadastrarGestor.as_view(), name="cadastrar_gestor"),

]
