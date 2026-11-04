# reportes/pdf_views.py
"""Generación de PDFs — W12.

Usa WeasyPrint para convertir un template HTML de Django
en un archivo PDF descargable.
"""
from io import BytesIO

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from weasyprint import HTML

from ventas.models import Venta


@login_required
def factura_pdf(request, venta_id):
    """Genera y devuelve el PDF de una factura.

    Args:
        venta_id: ID de la venta.

    Returns:
        HttpResponse con el PDF adjunto para descarga.
    """
    # 1. Obtener la venta con sus detalles precargados
    venta = get_object_or_404(
        Venta.objects
        .select_related('cliente')
        .prefetch_related('detalles__producto'),
        pk=venta_id,
    )

    # 2. Renderizar el template HTML
    html_string = render_to_string(
        'reportes/factura.html',
        {'venta': venta},
        request=request,
    )

    # 3. Convertir el HTML a PDF con WeasyPrint
    html = HTML(string=html_string, base_url=request.build_absolute_uri('/'))
    pdf_bytes = html.write_pdf()

    # 4. Devolver el PDF como descarga
    response = HttpResponse(pdf_bytes, content_type='application/pdf')
    response['Content-Disposition'] = (
        f'attachment; filename="factura_{venta.pk}.pdf"'
    )
    return response