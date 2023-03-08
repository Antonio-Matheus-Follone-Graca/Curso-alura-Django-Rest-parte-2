from rest_framework import viewsets,filters
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente

import django_filters.rest_framework

# bibliotecas responsáveis pela ordenação 
import django_filters.rest_framework

class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    # ordenando pelo campo nome
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['nome']
   

