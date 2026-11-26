## Sprint Backlog — actualización W16


| Tarea | Estado |
|---|---|
| pip install celery redis flower | ✅ W16 |
| core/celery.py + core/__init__.py | ✅ W16 |
| CELERY_* en settings.py (SSL para Upstash) | ✅ W16 |
| ventas/tasks.py (2 tareas placeholder) | ✅ W16 |
| pago_exitoso: .delay() al vaciar carrito | ✅ W16 |
| webhook: .delay() al confirmar pago | ✅ W16 |
| Tests W16 (7 tests) | ✅ W16 |
| SendGrid correo transaccional real | ⏳ W17 |
| Alerta de stock bajo por correo | ⏳ W17 |
| Celery Beat + tareas programadas | ⏳ W18 |


## Sprint Backlog — actualización W17


| Tarea | Estado |
|---|---|
| pip install celery redis flower | ✅ W16 |
| core/celery.py + tareas placeholder | ✅ W16 |
| pip install django-anymail | ✅ W17 |
| EMAIL_BACKEND configurado (console dev / resend prod) | ✅ W17 |
| correo_enviado en Pedido + migración 0004 | ✅ W17 |
| Templates confirmacion_pedido.html + .txt | ✅ W17 |
| Templates alerta_stock.html + .txt | ✅ W17 |
| enviar_confirmacion_pedido: correo real + idempotencia | ✅ W17 |
| verificar_stock_bajo: alerta al admin | ✅ W17 |
| 9 tests con mail.outbox | ✅ W17 |
| Celery Beat + tareas programadas | ⏳ W18 |