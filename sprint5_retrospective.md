# Sprint 5 Retrospective — ERP Django
## Semanas W16–W18 · Espiral 6: Celery e Integraciones


## ¿Qué funcionó bien? (Keep)
1. El campo correo_enviado en Pedido resolvió los duplicados.
2. @override_settings(EMAIL_BACKEND=locmem) hizo triviales los tests de correo.
3. Modo EAGER sin REDIS_URL para el laboratorio sin Docker.
4. El webhook como ÚNICO disparador del correo, con try/except.
5. Worker y Beat embebidos en el contenedor web con start.sh.


## ¿Qué mejorar? (Improve)
1. **Dependencias:** Fijar kombu==5.3.7 para evitar el VersionMismatch con redis==5.0.1.
2. **Variables de entorno:** Revisar la tabla de variables antes de desplegar.
3. **Render Free se duerme:** Beat no dispara mientras el servicio duerme.
4. **Pruebas antiguas:** Las fallas heredadas se corrigieron.


## Velocidad del Sprint 5
Puntos planificados: 18
Puntos entregados: 18
**Tests al cierre:** 174 (OK)