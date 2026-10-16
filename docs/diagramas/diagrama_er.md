# Diagrama Entidad-Relación — ERP Django
## Espiral 2

```mermaid
erDiagram
    CATEGORIA {
        bigint id PK
        varchar nombre UK
        text descripcion
    }
    PROVEEDOR {
        bigint id PK
        varchar nombre
        varchar correo UK
    }
    CLIENTE {
        bigint id PK
        varchar nombre
        varchar correo UK
    }
    PRODUCTO {
        bigint id PK
        varchar nombre
        decimal precio
        int stock
        bigint categoria_id FK
        bigint proveedor_id FK
    }
    VENTA {
        bigint id PK
        bigint cliente_id FK
        datetime fecha
    }
    DETALLE_VENTA {
        bigint id PK
        bigint venta_id FK
        bigint producto_id FK
        int cantidad
        decimal precio_unitario
    }
    PEDIDO {
        bigint id PK
        varchar numero_pedido UK
        bigint cliente_id FK
        varchar estado
    }
    CONFIGURACION_ERP {
        bigint id PK
        varchar nombre_empresa
        varchar moneda
    }

    CATEGORIA   ||--o{ PRODUCTO      : "clasifica"
    PROVEEDOR   |o--o{ PRODUCTO      : "suministra"
    CLIENTE     ||--o{ VENTA         : "realiza"
    CLIENTE     ||--o{ PEDIDO        : "genera"
    VENTA       ||--|{ DETALLE_VENTA : "contiene"
    PRODUCTO    ||--o{ DETALLE_VENTA : "incluido en"
```

## Cardinalidades

| Relación | Tipo |
|---|---|
| Categoria → Producto | 1:N obligatorio |
| Proveedor → Producto | 1:N opcional |
| Cliente → Venta | 1:N |
| Cliente → Pedido | 1:N |
| Venta → DetalleVenta | 1:N obligatorio |
| Producto → DetalleVenta | 1:N |