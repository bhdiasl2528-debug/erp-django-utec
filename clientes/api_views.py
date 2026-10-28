# clientes/api_views.py
"""Vistas de la API REST para clientes — W10."""
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models      import Cliente
from .serializers import ClienteSerializer


class ClienteListCreateAPIView(ListCreateAPIView):
    queryset         = Cliente.objects.filter(activo=True).order_by('nombre')
    serializer_class = ClienteSerializer


class ClienteDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset         = Cliente.objects.all()
    serializer_class = ClienteSerializer