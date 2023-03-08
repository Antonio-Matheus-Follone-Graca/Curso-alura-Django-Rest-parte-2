from rest_framework import viewsets
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente
from rest_framework import filters

import django_filters.rest_framework

# bibliotecas responsáveis pela ordenação 
import django_filters.rest_framework

class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    # ordenando pelo campo nome e busca por nome
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    # ordenação pelo campo nome
    ordering_fields = ['nome']
    # busca pelo campo nome e cpf
    search_fields = ['nome','cpf']
    # filtrando por campo ativo
    filterset_fields = ['ativo']
   

