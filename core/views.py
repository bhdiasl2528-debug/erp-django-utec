# core/views.py
"""Vistas de la app core — Página de inicio y bienvenida."""
from django.shortcuts import render


def bienvenida(request):
    """Página de inicio del ERP con tarjetas a los módulos principales."""
    modulos = [
        {
            'titulo': 'Productos',
            'descripcion': 'Inventario, precios y stock',
            'icono': '📦',
            'url': 'productos:lista',
        },
        {
            'titulo': 'Clientes',
            'descripcion': 'Cartera y gestión de clientes',
            'icono': '👥',
            'url': 'clientes:lista',
        },
        {
            'titulo': 'Proveedores',
            'descripcion': 'Red de proveedores',
            'icono': '🏭',
            'url': 'proveedores:lista',
        },
        {
            'titulo': 'Ventas',
            'descripcion': 'Pedidos, facturas y cobros',
            'icono': '💰',
            'url': 'ventas:lista',
        },
        {
            'titulo': 'Reportes',
            'descripcion': 'Dashboard y analítica',
            'icono': '📊',
            'url': 'admin:index',
        },
        {
            'titulo': 'Admin',
            'descripcion': 'Panel de administración Django',
            'icono': '⚙️',
            'url': 'admin:index',
        },
    ]
    
    # Usamos 'base.html' como plantilla de respaldo para que no falle
    return render(request, 'index.html', {'modulos': modulos})