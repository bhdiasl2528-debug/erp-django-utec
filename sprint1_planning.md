# Sprint 1 Planning — ERP Django
## Semanas W04–W06 · Espiral 2: Modelado de Datos y ORM

**Sprint Goal:**
Al finalizar el Sprint 1, el ERP tendrá un esquema de base de datos
completo implementado en Django, con 8 entidades, relaciones verificadas,
panel admin funcional y una suite de ≥ 15 pruebas de modelo pasando.

**Duración:** W04 (diseño) · W05 (implementación) · W06 (validación + M2)

---

## HUs seleccionadas del Product Backlog

| ID | Historia de Usuario | Puntos | Semana |
|---|---|---|---|
| HU-E2-01 | Diagrama ER aprobado | 3 | W04 |
| HU-E2-02 | Registrar clientes | 2 | W05 |
| HU-E2-03 | Registrar proveedores | 2 | W05 |
| HU-E2-04 | Registrar categorías | 1 | W05 |
| HU-E2-05 | Registrar productos | 3 | W05 |
| HU-E2-06 | Registrar ventas con detalle | 5 | W05 |
| HU-E2-07 | 15+ tests de modelo | 3 | W06 |
| HU-E2-08 | Panel admin con Jazzmin | 2 | W06 |

**Total de puntos del Sprint 1:** 21 puntos

---

## Sprint Backlog — Tareas técnicas

| Tarea | Semana | Estado |
|---|---|---|
| Diseñar diagrama ER (8 entidades) | W04 | ⏳ |
| Normalizar a 3FN y documentar decisiones | W04 | ⏳ |
| Obtener aprobación del asesor | W04 | ⏳ |
| Implementar models.py × 5 apps | W05 | ⏳ |
| Ejecutar makemigrations + migrate | W05 | ⏳ |
| Registrar modelos en admin.py | W05 | ⏳ |
| Agregar validators a campos críticos | W06 | ⏳ |
| Escribir tests/test_models.py (≥ 15 tests) | W06 | ⏳ |
| Instalar y configurar django-jazzmin | W06 | ⏳ |

---

## Definición de Terminado (DoD) — Sprint 1

- Diagrama ER aprobado formalmente por el asesor (firma en ficha)
- `python manage.py showmigrations` → `[X] 0001_initial` en cada app
- `/admin/` muestra las 8 entidades correctamente
- `python manage.py test tests.test_models` → ≥ 15 tests PASSED
- Precio negativo en Producto → `ValidationError`
- Correo duplicado en Cliente → `IntegrityError`
- `fichas/espiral_02_modelos.md` completa

---

## Sprint Backlog — actualización de estados W05

| Tarea | Estado |
|---|---|
| Diseño diagrama ER (8 entidades) | ✅ W04 |
| Normalizar 3FN + decisiones | ✅ W04 |
| Aprobación del asesor | ✅ W04 |
| Crear app configuracion | ✅ W05 |
| Implementar models.py × 6 apps | ✅ W05 |
| Ejecutar makemigrations + migrate | ✅ W05 |
| Registrar en admin.py | ✅ W05 |
| 12 smoke tests pasando | ✅ W05 |
| Agregar validators a campos críticos | ⏳ W06 |
| Suite completa ≥ 15 tests | ⏳ W06 |
| Instalar y configurar django-jazzmin | ⏳ W06 |