# Entidades y Atributos — ERP Django
## Espiral 2 · Referencia para W05

## Entidad 1 — Categoria

| Atributo | Tipo Django | Restricción |
|---|---|---|
| id | BigAutoField | PK, auto |
| nombre | CharField(100) | unique, not null |
| descripcion | TextField | blank=True |

## Entidad 2 — Proveedor

| Atributo | Tipo Django | Restricción |
|---|---|---|
| id | BigAutoField | PK, auto |
| nombre | CharField(150) | not null |
| contacto | CharField(100) | blank=True |
| correo | EmailField | unique, not null |
| telefono | CharField(20) | blank=True |
| activo | BooleanField | default=True |
| creado | DateTimeField | auto_now_add |

## Entidad 3 — Cliente

| Atributo | Tipo Django | Restricción |
|---|---|---|
| id | BigAutoField | PK, auto |
| nombre | CharField(150) | not null |
| correo | EmailField | unique, not null |
| telefono | CharField(20) | blank=True |
| activo | BooleanField | default=True |
| creado | DateTimeField | auto_now_add |

## Entidad 4 — Producto

| Atributo | Tipo Django | Restricción |
|---|---|---|
| id | BigAutoField | PK, auto |
| nombre | CharField(200) | not null |
| precio | DecimalField(10,2) | MinValueValidator(0) |
| stock | IntegerField | default=0, MinValue(0) |
| categoria | ForeignKey(Categoria) | PROTECT |
| proveedor | ForeignKey(Proveedor) | SET_NULL, null=True |
| activo | BooleanField | default=True |
| creado | DateTimeField | auto_now_add |

## Entidad 5 — Venta

| Atributo | Tipo Django | Restricción |
|---|---|---|
| id | BigAutoField | PK, auto |
| cliente | ForeignKey(Cliente) | PROTECT |
| fecha | DateTimeField | auto_now_add |
| total | Propiedad calculada | NO es campo de BD |

## Entidad 6 — DetalleVenta

| Atributo | Tipo Django | Restricción |
|---|---|---|
| id | BigAutoField | PK, auto |
| venta | ForeignKey(Venta) | CASCADE |
| producto | ForeignKey(Producto) | PROTECT |
| cantidad | PositiveIntegerField | >= 1 |
| precio_unitario | DecimalField(10,2) | not null |

## Entidad 7 — Pedido

| Atributo | Tipo Django | Restricción |
|---|---|---|
| id | BigAutoField | PK, auto |
| numero_pedido | CharField(20) | unique |
| cliente | ForeignKey(Cliente) | PROTECT |
| estado | CharField(20) | choices |
| fecha_pedido | DateTimeField | auto_now_add |
| fecha_entrega | DateField | null=True |
| total_pagado | DecimalField(10,2) | null=True |

## Entidad 8 — ConfiguracionERP

| Atributo | Tipo Django | Restricción |
|---|---|---|
| id | BigAutoField | PK, auto |
| nombre_empresa | CharField(200) | not null |
| rfc | CharField(13) | blank=True |
| moneda | CharField(3) | default='MXN' |
| iva_porcentaje | DecimalField(5,2) | default=16.00 |
| logo | ImageField | null=True, blank=True |