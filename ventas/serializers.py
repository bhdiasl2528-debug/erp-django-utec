# ventas/serializers.py
"""Serializers de la app ventas — W10."""
from decimal import Decimal

from rest_framework import serializers

from .models import DetalleVenta, Venta


class DetalleVentaSerializer(serializers.ModelSerializer):
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model  = DetalleVenta
        fields = ['id', 'producto', 'cantidad',
                  'precio_unitario', 'subtotal']
        read_only_fields = ['id', 'subtotal']

    def get_subtotal(self, obj: DetalleVenta) -> Decimal:
        return obj.subtotal


class VentaSerializer(serializers.ModelSerializer):
    detalles      = DetalleVentaSerializer(many=True, read_only=True)
    total         = serializers.SerializerMethodField()
    cliente_nombre = serializers.CharField(source='cliente.nombre', read_only=True)

    class Meta:
        model  = Venta
        fields = ['id', 'cliente', 'cliente_nombre',
                  'fecha', 'detalles', 'total']
        read_only_fields = ['id', 'fecha', 'detalles',
                            'total', 'cliente_nombre']

    def get_total(self, obj: Venta) -> Decimal:
        return obj.total