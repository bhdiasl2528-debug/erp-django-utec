# api/views.py
"""ViewSets de la API REST — W10."""
from rest_framework import viewsets

from .serializers import (
    CategoriaSerializer,
    ClienteSerializer,
    ConfiguracionERPSerializer,
    DetalleVentaSerializer,
    PedidoSerializer,
    ProductoSerializer,
    ProveedorSerializer,
    VentaSerializer,
)
from clientes.models       import Cliente
from configuracion.models  import ConfiguracionERP
from productos.models      import Categoria, Producto
from proveedores.models    import Proveedor
from ventas.models         import DetalleVenta, Pedido, Venta


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('nombre')
    serializer_class = ClienteSerializer


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all().order_by('nombre')
    serializer_class = ProveedorSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by('nombre')
    serializer_class = CategoriaSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.select_related('categoria', 'proveedor').all().order_by('nombre')
    serializer_class = ProductoSerializer


class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.select_related('cliente').prefetch_related('detalles__producto').all()
    serializer_class = VentaSerializer


class DetalleVentaViewSet(viewsets.ModelViewSet):
    queryset = DetalleVenta.objects.select_related('producto').all()
    serializer_class = DetalleVentaSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.select_related('cliente').all().order_by('-fecha_pedido')
    serializer_class = PedidoSerializer


class ConfiguracionERPViewSet(viewsets.ModelViewSet):
    queryset = ConfiguracionERP.objects.all()
    serializer_class = ConfiguracionERPSerializer