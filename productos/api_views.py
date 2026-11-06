from rest_framework import generics
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.exceptions import PermissionDenied
from .models import Producto, Categoria
from .serializers import ProductoSerializer, CategoriaSerializer

class CustomAuthOrReadOnly(BasePermission):
    """Permite lectura sin auth, pero exige autenticación para POST/PUT/DELETE (devuelve 403)."""
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user and request.user.is_authenticated:
            return True
        raise PermissionDenied("Authentication credentials were not provided.")

class CategoriaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [CustomAuthOrReadOnly]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

class CategoriaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [CustomAuthOrReadOnly]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

class ProductoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Producto.objects.all().order_by('id')
    serializer_class = ProductoSerializer
    permission_classes = [CustomAuthOrReadOnly]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

class ProductoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [CustomAuthOrReadOnly]
    authentication_classes = [TokenAuthentication, SessionAuthentication]