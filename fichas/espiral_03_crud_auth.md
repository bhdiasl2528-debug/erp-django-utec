# Ficha de Sistematización — Espiral 3
## ERP Django · Espiral E3: CRUD Web y Autenticación

| Campo | Contenido |
|---|---|
| **Número de espiral** | 3 |
| **Nombre del ciclo** | CRUD Web y Autenticación |
| **Semanas** | W07 – W09 |
| **Fecha de inicio** | 20/10/2026 |
| **Fecha de cierre** | 21/10/2026 |
| **Responsable** | Brandon Horacio Dias López |
| **Asesor** | MC. Román Fernando López González |

## 1. Objetivo del ciclo
Implementar la interfaz web completa del ERP con vistas de lectura
y escritura, formularios validados, autenticación mediante allauth
y control de acceso por rol (RBAC) con 3 grupos de usuarios.

## 2. Tareas realizadas

| # | Tarea | Estado | Semana |
|---|---|---|---|
| 1 | ListView + DetailView × 4 entidades | ✅ | W07 |
| 2 | 8 templates lista + detalle Fable 5 | ✅ | W07 |
| 3 | select_related anti-N+1 | ✅ | W07 |
| 4 | forms.py × 4 apps (ModelForm) | ✅ | W08 |
| 5 | Create/Update/Delete × 3 entidades | ✅ | W08 |
| 6 | crear_venta (función) | ✅ | W08 |
| 7 | messages flash en CRUD | ✅ | W08 |
| 8 | django-allauth instalado | ✅ | W09 |
| 9 | Templates login/signup Fable 5 | ✅ | W09 |
| 10 | Management command crear_grupos | ✅ | W09 |
| 11 | PermissionRequiredMixin en Delete | ✅ | W09 |
| 12 | @login_required + @permission_required | ✅ | W09 |
| 13 | 9 tests RBAC | ✅ | W09 |

## 3. Evidencias
- URL pública: https://erp-django-utec.onrender.com
- Login funcional: /accounts/login/
- Tests: Ran 99 tests → OK
- Grupos: Gerente / Vendedor / Almacen en /admin/

## 4. Criterios de aceptación

| Criterio | Estado |
|---|---|
| GET /productos/ sin login → solo lectura | ✅ |
| GET /productos/eliminar/ sin permiso → 403 | ✅ |
| Gerente → acceso completo | ✅ |
| Vendedor → solo ventas y consulta | ✅ |
| 99 tests acumulados OK | ✅ |

## 5. Problemas encontrados
| Problema | Causa | Solución |
|---|---|---|
| `Unknown command: crear_grupos` | `core` no estaba en INSTALLED_APPS | Agregar `'core'` a INSTALLED_APPS |
| Test `test_eliminar_producto_sin_auth_redirige_a_login` fallaba con 403 | `raise_exception = True` devuelve 403 incluso para anónimos | Corregir el test para esperar 403 |
| Tests W08 fallaban con 403 | Los usuarios no tenían permisos tras W09 | Agregar `.user_permissions.add(...)` en los tests |
| Admin en Render daba 500 | Jazzmin 3.0.5 con `.map` faltante | Downgrade a Jazzmin 2.6.2 |

## 6. Lecciones aprendidas
1. `PermissionRequiredMixin` con `raise_exception = True` devuelve 403 incluso para usuarios anónimos. Es el comportamiento correcto.
2. Los management commands solo se descubren si la app está en `INSTALLED_APPS`.
3. Los tests viejos deben actualizarse cuando agregamos seguridad (RBAC).

## 7. Tiempo total invertido

| Categoría | Horas |
|---|---|
| Diseño | ~2 h |
| Implementación | ~8 h |
| Pruebas | ~4 h |
| Documentación | ~2 h |
| **Total Espiral 3** | **~16 h** |

## 8. Aprobación formal

| Rol | Nombre | Fecha | Observaciones |
|---|---|---|---|
| Desarrollador | Brandon Horacio Dias López | 21/10/2026 | |
| **Asesor (PO)** | **MC. Román Fernando López González** | ___/___/_____ | Pendiente revisión formal |

> ⚠️ **Hito M3 alcanzado:** CRUD completo + auth + 3 roles + 99 tests OK + login Fable 5.