# Sprint 1 Retrospective — ERP Django
## Semanas W04–W06 · Espiral 2: Modelado de Datos y ORM

**Fecha:** 19/10/2026
**Facilitador/Scrum Master:** Brandon Horacio Dias López

## ¿Qué funcionó bien? (Keep)
1. Diseñar el ER en papel (W04) antes de escribir código evitó errores de FK y de 3FN.
2. Los smoke tests de W05 (12) detectaron a tiempo el bug del `precio_unitario is None`.
3. Jazzmin mejoró muchísimo la UX del admin con muy poca configuración.

## ¿Qué mejorar? (Improve)
1. Documentar el diagrama ER con más detalle (agregar cardinalidades explícitas) antes de la revisión.
2. Ejecutar `full_clean()` en los tests desde el principio, no solo `save()`, para validar correctamente.
3. Tener un `hotspot` o red alterna a la mano cuando el WiFi del taller bloquee GitHub.

## ¿Qué eliminar? (Drop)
1. Los archivos temporales sueltos en la raíz (`diagrama_er.png` duplicado) — mantener solo los que están en `evidencias/`.

## Acción de mejora (Kaizen) para Sprint 2
> "En el Sprint 2 (vistas CBV), voy a crear primero los templates `lista.html` y `detalle.html` en una carpeta común antes de escribir las vistas, para reutilizarlas y evitar duplicación de HTML."

## Velocidad del Sprint 1

| HU | Puntos planificados | Puntos entregados |
|---|---|---|
| HU-E2-01 Diagrama ER aprobado | 3 | 3 |
| HU-E2-02 Modelo Cliente | 2 | 2 |
| HU-E2-03 Modelo Proveedor | 2 | 2 |
| HU-E2-04 Modelo Categoria | 1 | 1 |
| HU-E2-05 Modelo Producto | 3 | 3 |
| HU-E2-06 Modelos Venta + Detalle | 5 | 5 |
| HU-E2-07 Suite ≥ 15 tests | 3 | 3 |
| HU-E2-08 Admin con Jazzmin | 2 | 2 |
| **Total** | **21** | **21** |

**Velocidad del equipo Sprint 1:** 21 puntos
**Velocidad acumulada (S0 + S1):** 31 puntos

## Métricas técnicas al cierre

- Modelos implementados: 8 (`Cliente`, `Proveedor`, `Categoria`, `Producto`, `Venta`, `DetalleVenta`, `Pedido`, `ConfiguracionERP`)
- Migraciones aplicadas: 6 (5 × `0001_initial` + 1 × `0002_validators_pedido`)
- Tests pasando: 72 (W01–W06)
- URL pública: `https://erp-django-utec.onrender.com`
- Tema del admin: Jazzmin 3.0.5 con paleta Fable 5 AzulERP