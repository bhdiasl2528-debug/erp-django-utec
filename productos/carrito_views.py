# productos/carrito_views.py
"""Vistas del carrito de compras — W12."""
from django.contrib import messages
from django.shortcuts import redirect, render

from .carrito import (
    agregar_producto,
    quitar_producto,
    total_items,
    total_precio,
    vaciar_carrito,
)


def ver_carrito(request):
    """Página del carrito con todos los productos."""
    carrito = request.session.get('carrito', {})
    return render(request, 'productos/carrito.html', {
        'carrito':       carrito,
        'total_items':   total_items(carrito),
        'total_precio':  total_precio(carrito),
    })


def agregar_al_carrito(request, producto_id):
    """Agrega un producto al carrito y regresa a la página anterior."""
    carrito = agregar_producto(request, producto_id, cantidad=1)
    messages.success(
        request,
        f'Producto agregado al carrito. Total: {total_items(carrito)} items.'
    )
    return redirect(request.META.get('HTTP_REFERER', 'productos:lista'))


def quitar_del_carrito(request, producto_id):
    """Quita un producto del carrito."""
    quitar_producto(request, producto_id)
    messages.success(request, 'Producto eliminado del carrito.')
    return redirect('productos:ver_carrito')


def vaciar(request):
    """Vacía todo el carrito."""
    vaciar_carrito(request)
    messages.success(request, 'Carrito vaciado.')
    return redirect('productos:ver_carrito')