# api/serializers.py
"""Serializers de la API REST — W10."""
from rest_framework import serializers

from clientes.models       import Cliente
from configuracion.models  import ConfiguracionERP
from productos.models      import Categoria, Producto
from proveedores.models    import Proveedor
from ventas.models         import DetalleVenta, Pedido, Venta


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Cliente
        fields = ['id', 'nombre', 'correo', 'telefono', 'activo', 'creado']
        read_only_fields = ['id', 'creado']


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Proveedor
        fields = ['id', 'nombre', 'contacto', 'correo', 'telefono', 'activo', 'creado']
        read_only_fields = ['id', 'creado']


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Categoria
        fields = ['id', 'nombre', 'descripcion']
        read_only_fields = ['id']


class ProductoSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)
    proveedor_nombre = serializers.CharField(source='proveedor.nombre', read_only=True, allow_null=True)

    class Meta:
        model  = Producto
        fields = [
            'id', 'nombre', 'precio', 'stock',
            'categoria', 'categoria_nombre',
            'proveedor', 'proveedor_nombre',
            'activo', 'creado',
        ]
        read_only_fields = ['id', 'creado', 'categoria_nombre', 'proveedor_nombre']


class DetalleVentaSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)
    subtotal        = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)

    class Meta:
        model  = DetalleVenta
        fields = ['id', 'producto', 'producto_nombre', 'cantidad', 'precio_unitario', 'subtotal']
        read_only_fields = ['id', 'producto_nombre', 'subtotal']


class VentaSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='cliente.nombre', read_only=True)
    total          = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)
    detalles       = DetalleVentaSerializer(many=True, read_only=True)

    class Meta:
        model  = Venta
        fields = ['id', 'cliente', 'cliente_nombre', 'fecha', 'total', 'detalles']
        read_only_fields = ['id', 'fecha', 'total', 'cliente_nombre', 'detalles']


class PedidoSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='cliente.nombre', read_only=True)
    estado_display = serializers.CharField(source='get_estado_display', read_only=True)

    class Meta:
        model  = Pedido
        fields = [
            'id', 'numero_pedido', 'cliente', 'cliente_nombre',
            'estado', 'estado_display',
            'fecha_pedido', 'fecha_entrega', 'total_pagado',
        ]
        read_only_fields = ['id', 'fecha_pedido', 'cliente_nombre', 'estado_display']


class ConfiguracionERPSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ConfiguracionERP
        fields = ['id', 'nombre_empresa', 'rfc', 'moneda', 'iva_porcentaje', 'logo']
        read_only_fields = ['id']