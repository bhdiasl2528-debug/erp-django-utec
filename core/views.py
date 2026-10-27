# core/views.py
"""Vistas de la app core — Página de inicio y bienvenida."""
from django.shortcuts import render
from productos.models import Producto


def bienvenida(request):
    """Página de inicio del ERP con tarjetas a los módulos principales."""
    modulos = [
        {'titulo': 'Catálogo', 'descripcion': 'Inventario de zapatos', 'icono': '👟', 'url': 'productos:lista'},
        {'titulo': 'Clientes', 'descripcion': 'Cartera de clientes', 'icono': '👥', 'url': 'clientes:lista'},
        {'titulo': 'Proveedores', 'descripcion': 'Fabricantes y distribuidores', 'icono': '🏭', 'url': 'proveedores:lista'},
        {'titulo': 'Ventas', 'descripcion': 'Pedidos y facturación', 'icono': '💳', 'url': 'ventas:lista'},
        {'titulo': 'Reportes', 'descripcion': 'Análisis de ventas', 'icono': '📊', 'url': 'admin:index'},
        {'titulo': 'Admin', 'descripcion': 'Panel de administración', 'icono': '⚙️', 'url': 'admin:index'},
    ]

    # Obtener los últimos 6 productos activos de la BD
    productos_destacados = (
        Producto.objects
        .filter(activo=True)
        .select_related('categoria')
        .order_by('-creado')[:6]
    )

    return render(request, 'index.html', {
        'modulos': modulos,
        'productos_destacados': productos_destacados,
    })


def cargar_zapatos_view(request):
    """Vista temporal para cargar productos de zapatos en producción."""
    from django.core.management import call_command
    from io import StringIO
    from django.http import HttpResponse

    out = StringIO()
    try:
        call_command('cargar_zapatos', stdout=out)
        return HttpResponse(f"<pre>{out.getvalue()}</pre>")
    except Exception as e:
        return HttpResponse(f"<pre>ERROR: {e}</pre>")