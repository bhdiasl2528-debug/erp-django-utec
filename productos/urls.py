# productos/urls.py
"""URLs de la app productos — W12 (con carrito)."""
from django.urls import path
from . import views, carrito_views

app_name = 'productos'

urlpatterns = [
    # Lectura
    path('', views.ProductoListView.as_view(), name='lista'),
    path('<int:producto_id>/', views.ProductoDetailView.as_view(), name='detalle'),
    # Escritura
    path('nuevo/', views.ProductoCreateView.as_view(), name='crear'),
    path('<int:producto_id>/editar/', views.ProductoUpdateView.as_view(), name='editar'),
    path('<int:producto_id>/eliminar/', views.ProductoDeleteView.as_view(), name='eliminar'),
    # Carrito
    path('carrito/', carrito_views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:producto_id>/', carrito_views.agregar_al_carrito, name='agregar_carrito'),
    path('carrito/quitar/<int:producto_id>/', carrito_views.quitar_del_carrito, name='quitar_carrito'),
    path('carrito/vaciar/', carrito_views.vaciar, name='vaciar_carrito'),
]