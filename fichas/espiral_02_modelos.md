# Ficha de Sistematización — Espiral 2
## ERP Django · Espiral E2: Modelado de Datos y ORM
## UTEC Celaya · Técnico en Programación (SEP 3061300006-23)

| Campo | Contenido |
|---|---|
| **Número de espiral** | 2 |
| **Nombre del ciclo** | Modelado de Datos y ORM |
| **Semanas** | W04 – W06 |
| **Fecha de inicio** | 15/10/2026 |
| **Fecha de cierre** | 19/10/2026 |
| **Responsable** | Brandon Horacio Dias López |
| **Asesor** | MC. Román Fernando López González |

---

## 1. Objetivo del ciclo

Diseñar, implementar y validar el esquema de base de datos completo del
ERP en Django, garantizando integridad referencial, normalización 3FN y
cobertura de pruebas ≥ 15 tests de modelo.

**Estado:** ✅ Cumplido. Se implementaron 8 modelos, 6 migraciones y 17 tests de modelo (más los 55 heredados de la Espiral 1).

---

## 2. Tareas realizadas

| # | Tarea | Estado | Tiempo invertido |
|---|---|---|---|
| 1 | Diseño diagrama ER (8 entidades) | ✅ W04 | ~2 h |
| 2 | Normalización 3FN y decisiones de diseño | ✅ W04 | ~1 h |
| 3 | Aprobación verbal del asesor | ✅ W04 | — |
| 4 | Implementar models.py × 6 apps | ✅ W05 | ~3 h |
| 5 | Ejecutar makemigrations + migrate | ✅ W05 | ~1 h |
| 6 | Registrar en admin.py | ✅ W05 | ~1.5 h |
| 7 | Agregar validators + clean() | ✅ W06 | ~1 h |
| 8 | Suite de ≥ 15 tests de modelo | ✅ W06 | ~2 h |
| 9 | Instalar y configurar django-jazzmin | ✅ W06 | ~1.5 h |

---

## 3. Evidencias generadas

- [x] Diagrama ER aprobado: `docs/diagramas/diagrama_er.md`
- [x] Imagen exportada: `evidencias/espiral_02/diagrama_er.png`
- [x] Decisiones de diseño: `docs/decisiones_diseno.md`
- [x] Tabla de entidades: `docs/entidades_atributos.md`
- [x] Migraciones: `*/migrations/0001_initial.py` × 5 apps + `ventas/migrations/0002_validators_pedido.py`
- [x] Tests: `tests/test_w05_modelos.py` (12 OK) + `tests/test_w06_validadores.py` (17 OK)
- [x] Output de tests: `evidencias/espiral_02/tests_72_ok.txt`
- [x] Admin con Jazzmin: `https://erp-django-utec.onrender.com/admin/`
- [x] Captura del admin: `evidencias/espiral_02/jazzmin_admin.png`
- [x] Commit final: `a24ddcf Sprint 1 W06: clean() + Jazzmin + 72 tests OK [pre-M2]`

---

## 4. Criterios de aceptación (verificados en W06)

| Criterio | Estado | Evidencia |
|---|---|---|
| Diagrama ER aprobado por el asesor | ✅ | Aprobación verbal 16/10/2026 |
| `showmigrations` → `[X] 0001_initial` en 5 apps | ✅ | Terminal |
| `[X] 0002_validators_pedido` en ventas | ✅ | Terminal |
| `/admin/` muestra las 8 entidades con Jazzmin | ✅ | Captura del admin |
| ≥ 15 tests de modelo PASSED | ✅ | 17 tests en W06 (72 acumulados) |
| Precio negativo → ValidationError | ✅ | `test_precio_negativo_lanza_validation_error` |
| Correo duplicado → IntegrityError | ✅ | `test_correo_duplicado_cliente_lanza_integrity_error` |
| Migración aplicada en producción | ✅ | Logs de Render |

---

## 5. Problemas encontrados y soluciones

| Problema | Causa | Solución aplicada |
|---|---|---|
| `save()` no ejecuta validators | Comportamiento normal de Django | Se usó `full_clean()` explícito en los tests |
| Migración en producción pendiente al primer intento | Red del taller bloqueaba GitHub | Se usó hotspot del celular como red alterna |
| `.git` se perdía entre sesiones | Script `iniciar_sesion.bat` con `xcopy /s /e` sin `/h` | Se agregó `/h` a ambos scripts (backup PC↔USB) |
| Warning de Jazzmin sobre `dark_mode_theme` deprecado | Jazzmin 3.0.5 cambió la API de temas | Se comentó la línea obsoleta |

---

## 6. Lecciones aprendidas

1. **`full_clean()` vs `save()`:** los validators solo se ejecutan con `full_clean()` (o a través del admin, que lo llama implícitamente). `save()` directo en código Python no valida nada — hay que ser explícito en los tests.

2. **Patrón singleton con `save()` sobreescrito:** es efectivo pero hay que saber que `get_or_create(pk=1)` es necesario para que no falle si el registro ya existe. Y en el admin hay que deshabilitar `has_add_permission`.

3. **Jazzmin mejora la UX del admin drásticamente con muy poca configuración:** el `custom_css` permite llevar la paleta Fable 5 AzulERP sin necesidad de reescribir templates del admin.

---

## 7. Tiempo total invertido

| Categoría | Horas |
|---|---|
| Diseño / planeación | ~3 h |
| Implementación | ~6 h |
| Pruebas | ~4 h |
| Despliegue | ~1 h |
| Documentación | ~2 h |
| **Total Espiral 2** | **~16 h** |

---

## 8. Aprobación formal del diagrama ER

| Rol | Nombre | Fecha | Observaciones |
|---|---|---|---|
| Desarrollador | Brandon Horacio Dias López | 16/10/2026 | |
| **Asesor (PO)** | **MC. Román Fernando López González** | 16/10/2026 | **Aprobación verbal** — indicó avanzar W04, W05 y W06, revisión conjunta posterior |

> ⚠️ **Hito M2 alcanzado:** esquema ER aprobado, migraciones aplicadas (dev + prod), 72 tests OK, admin con Jazzmin y documentación completa.

---

## 9. Conexión con el trabajo recepcional

> Esta espiral aporta evidencia para el **Capítulo 4** (Desarrollo), sección 4.2 "Espiral 2: Modelado de Datos y ORM", y para el **Capítulo 3** (Metodología), subsección "Ciclos del modelo espiral — cierre del ciclo 2 con Hito M2".