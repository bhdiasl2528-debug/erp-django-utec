# productos/api_views.py
"""Vistas de la API REST para la app productos — W10."""
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models       import Categoria, Producto
from .serializers  import CategoriaSerializer, ProductoSerializer


class CategoriaListCreateAPIView(ListCreateAPIView):
    queryset         = Categoria.objects.all().order_by('nombre')
    serializer_class = CategoriaSerializer


class CategoriaDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset         = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProductoListCreateAPIView(ListCreateAPIView):
    serializer_class = ProductoSerializer

    def get_queryset(self):
        return (
            Producto.objects
            .select_related('categoria', 'proveedor')
            .filter(activo=True)
            .order_by('nombre')
        )


class ProductoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductoSerializer

    def get_queryset(self):
        return Producto.objects.select_related('categoria', 'proveedor')