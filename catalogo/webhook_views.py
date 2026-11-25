import logging
import stripe
from django.conf import settings
from django.db.models import F
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from productos.models import Producto
from ventas.models import Pedido
from ventas.tasks import enviar_confirmacion_pedido

logger = logging.getLogger(__name__)

@csrf_exempt
@require_POST
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE', '')

    try:
        event = stripe.Webhook.construct_event(
            payload=payload, sig_header=sig_header, secret=settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        return HttpResponse('Payload inválido.', status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse('Firma inválida.', status=400)

    tipo = event['type']
    if tipo == 'payment_intent.succeeded':
        _manejar_pago_exitoso(event['data']['object'])
    elif tipo == 'payment_intent.payment_failed':
        _manejar_pago_fallido(event['data']['object'])

    return HttpResponse(status=200)

def _manejar_pago_exitoso(payment_intent):
    pedido_id = _extraer_pedido_id(payment_intent)
    if pedido_id is None: return
    try:
        pedido = Pedido.objects.get(pk=pedido_id)
    except Pedido.DoesNotExist:
        return

    if pedido.estado != 'pagado':
        pedido.estado = 'pagado'
        pedido.save(update_fields=['estado'])
        _descontar_stock(pedido)

        try:
            enviar_confirmacion_pedido.delay(pedido.pk)
        except Exception:
            logger.exception(f'Webhook: no se pudo encolar la confirmación del pedido {pedido.numero_pedido} (¿Redis disponible?).')

def _manejar_pago_fallido(payment_intent):
    pedido_id = _extraer_pedido_id(payment_intent)
    if pedido_id is None: return
    try:
        pedido = Pedido.objects.get(pk=pedido_id)
    except Pedido.DoesNotExist:
        return
    if pedido.estado == 'pendiente':
        pedido.estado = 'cancelado'
        pedido.save(update_fields=['estado'])

def _extraer_pedido_id(payment_intent):
    try:
        pi_dict = payment_intent.to_dict() if hasattr(payment_intent, 'to_dict') else payment_intent
        pedido_id = pi_dict.get('metadata', {}).get('pedido_id')
    except Exception as e:
        logger.error(f'Error al leer metadata de Stripe: {e}')
        return None
    if not pedido_id:
        return None
    try:
        return int(pedido_id)
    except (ValueError, TypeError):
        return None

def _descontar_stock(pedido):
    for item in pedido.items_snapshot or []:
        prod_id = item.get('producto_id')
        cant = int(item.get('cantidad', 0))
        if not prod_id or cant <= 0: continue
        Producto.objects.filter(pk=prod_id, stock__gte=cant).update(stock=F('stock') - cant)