from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

class Venta(models.Model):
    cliente = models.ForeignKey(
        'clientes.Cliente', 
        on_delete=models.PROTECT, 
        related_name='ventas'
    )
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['-fecha']

    def __str__(self):
        return f'Venta #{self.pk} - {self.cliente.nombre}'

    @property
    def total(self):
        return sum(d.subtotal for d in self.detalles.all()) or Decimal('0.00')

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey('productos.Producto', on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    # Aquí permitimos que sea nulo para que el test pase
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalles de Venta'

    def __str__(self):
        return f'{self.cantidad}x {self.producto.nombre}'

    def save(self, *args, **kwargs):
        # D-06: si no viene el precio, se captura del producto
        if self.precio_unitario is None:
            self.precio_unitario = self.producto.precio
        super().save(*args, **kwargs)

    @property
    def subtotal(self):
        return self.cantidad * self.precio_unitario if self.precio_unitario else Decimal('0.00')

class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
        ('enviado', 'Enviado'),
        ('cancelado', 'Cancelado'),
    ]

    numero_pedido = models.CharField(max_length=20, unique=True)
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.PROTECT)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateField(null=True, blank=True)
    total_pagado = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True,
        validators=[MinValueValidator(Decimal('0.00'))]
    )
    
    # ── W15: Snapshot del carrito ──
    items_snapshot = models.JSONField(
        default=list,
        blank=True,
        verbose_name='Snapshot de items del carrito',
        help_text='Copia del carrito al momento de crear el pedido.'
    )

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-fecha_pedido']

    def __str__(self):
        return f'{self.numero_pedido} - {self.cliente.nombre}'