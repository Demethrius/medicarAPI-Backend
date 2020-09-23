from django.urls import path

from user.views import CadastrarCliente

urlpatterns = [
    path('cadastrar_cliente/', CadastrarCliente.as_view(), name="cadastrar_cliente"),

]
