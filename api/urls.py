
# api/urls.py
"""URLs de la API REST — W10."""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'clientes',       views.ClienteViewSet,        basename='api-clientes')
router.register(r'proveedores',    views.ProveedorViewSet,      basename='api-proveedores')
router.register(r'categorias',     views.CategoriaViewSet,      basename='api-categorias')
router.register(r'productos',      views.ProductoViewSet,       basename='api-productos')
router.register(r'ventas',         views.VentaViewSet,          basename='api-ventas')
router.register(r'detalles',       views.DetalleVentaViewSet,   basename='api-detalles')
router.register(r'pedidos',        views.PedidoViewSet,         basename='api-pedidos')
router.register(r'configuracion',  views.ConfiguracionERPViewSet, basename='api-configuracion')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]