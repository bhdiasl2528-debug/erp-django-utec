# productos/carrito.py
"""Lógica del carrito de compras basado en sesiones — W12.

El carrito se guarda en `request.session['carrito']` como un dict:
    { 'producto_id': {'cantidad': 1, 'precio': '250.00'}, ... }

No se usa base de datos para el MVP académico.
En la Espiral 5 se migrará a modelos Carrito/ItemCarrito.
"""
from decimal import Decimal

from productos.models import Producto


SESSION_KEY = 'carrito'


def _get_carrito(session) -> dict:
    """Devuelve el carrito actual desde la sesión."""
    return session.get(SESSION_KEY, {})


def agregar_producto(request, producto_id: int, cantidad: int = 1) -> dict:
    """Agrega un producto al carrito (o incrementa su cantidad)."""
    producto = Producto.objects.filter(pk=producto_id, activo=True).first()
    if not producto:
        return request.session.get(SESSION_KEY, {})

    carrito = request.session.get(SESSION_KEY, {})
    pid = str(producto_id)

    if pid in carrito:
        carrito[pid]['cantidad'] += cantidad
    else:
        carrito[pid] = {
            'nombre':   producto.nombre,
            'precio':   str(producto.precio),
            'cantidad': cantidad,
        }

    request.session[SESSION_KEY] = carrito
    request.session.modified = True
    return carrito


def quitar_producto(request, producto_id: int) -> dict:
    """Elimina un producto del carrito."""
    carrito = request.session.get(SESSION_KEY, {})
    pid = str(producto_id)
    if pid in carrito:
        del carrito[pid]
    request.session[SESSION_KEY] = carrito
    request.session.modified = True
    return carrito


def vaciar_carrito(request) -> None:
    """Vacía todo el carrito."""
    request.session[SESSION_KEY] = {}
    request.session.modified = True


def total_items(carrito: dict) -> int:
    """Devuelve el número total de unidades en el carrito."""
    return sum(item.get('cantidad', 0) for item in carrito.values())


def total_precio(carrito: dict) -> Decimal:
    """Devuelve el total monetario del carrito."""
    total = Decimal('0.00')
    for item in carrito.values():
        total += Decimal(item['precio']) * item['cantidad']
    return total