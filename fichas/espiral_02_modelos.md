# Ficha de Sistematización — Espiral 2
## ERP Django · Espiral E2: Modelado de Datos y ORM
## UTEC Celaya · Técnico en Programación (SEP 3061300006-23)

| Campo | Contenido |
|---|---|
| **Número de espiral** | 2 |
| **Nombre del ciclo** | Modelado de Datos y ORM |
| **Semanas** | W04 – W06 |
| **Fecha de inicio** | 15/10/2026 |
| **Fecha de cierre** | (completar en W06) |
| **Responsable** | [Tu nombre completo] |
| **Asesor** | MC. Román Fernando López González |

---

## 1. Objetivo del ciclo

Diseñar, implementar y validar el esquema de base de datos completo del
ERP en Django, garantizando integridad referencial, normalización 3FN y
cobertura de pruebas ≥ 15 tests de modelo.

---

## 2. Tareas realizadas

| # | Tarea | Estado | Tiempo invertido |
|---|---|---|---|
| 1 | Diseño diagrama ER (8 entidades) | ✅ W04 | ___ h |
| 2 | Normalización 3FN y decisiones de diseño | ✅ W04 | ___ h |
| 3 | Aprobación del asesor | ⏳ W04 | — |
| 4 | Implementar models.py × 5 apps | ⏳ W05 | — |
| 5 | Ejecutar makemigrations + migrate | ⏳ W05 | — |
| 6 | Registrar en admin.py | ⏳ W05 | — |
| 7 | Agregar validators | ⏳ W06 | — |
| 8 | Suite de ≥ 15 tests de modelo | ⏳ W06 | — |
| 9 | Instalar django-jazzmin | ⏳ W06 | — |

---

## 3. Evidencias generadas

- [x] Diagrama ER aprobado: `docs/diagramas/diagrama_er.md`
- [x] Imagen exportada: `evidencias/espiral_02/diagrama_er.png`
- [x] Decisiones de diseño: `docs/decisiones_diseno.md`
- [x] Tabla de entidades: `docs/entidades_atributos.md`
- [x] Output tests: `evidencias/espiral_02/tests_43_ok.txt`
- [ ] Migraciones: `*/migrations/0001_initial.py` × 5 apps
- [ ] Tests de modelo: `tests/test_models.py` — ___/15 OK

---

## 4. Criterios de aceptación (se verifican en W06)

| Criterio | Estado | Evidencia |
|---|---|---|
| Diagrama ER aprobado por el asesor | ⏳ | Firma en ficha |
| `showmigrations` → `[X] 0001_initial` en 5 apps | ⏳ | Terminal |
| `/admin/` muestra las 8 entidades | ⏳ | Captura |
| ≥ 15 tests de modelo PASSED | ⏳ | pytest output |
| Precio negativo → ValidationError | ⏳ | Test específico |
| Correo duplicado → IntegrityError | ⏳ | Test específico |

---

## 5. Problemas encontrados y soluciones (W04)

| Problema | Causa | Solución aplicada |
|---|---|---|
| Inconsistencia entre guía y test W03 (`DEBUG = False`) | El test busca espacios exactos | Se ajustó el archivo para coincidir |
| Dependencias faltantes en requirements.txt | No se congelaron en W02 | `pip install` + `pip freeze > requirements.txt` |
| Output de tests no capturado con `>` | Django envía resumen a stderr | Se usó `2>&1` para redirigir ambos flujos |

---

## 6. Lecciones aprendidas
(completar al cerrar en W06)

1.
2.
3.

---

## 7. Tiempo total invertido
(completar al cerrar en W06)

| Categoría | Horas |
|---|---|
| Diseño / planeación | |
| Implementación | |
| Pruebas | |
| Documentación | |
| **Total Espiral 2** | |

---

## 8. Aprobación formal del diagrama ER

| Rol | Nombre | Fecha | Observaciones |
|---|---|---|---|
| Desarrollador | [Tu nombre] | 15/10/2026 | |
| **Asesor (PO)** | **MC. Román Fernando López González** | ___/___/_____ | Pendiente |

> ⚠️ **La Espiral 2 (W05) no puede iniciar sin la aprobación registrada aquí.**