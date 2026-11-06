from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from ventas.models import Venta

# Intentamos importar WeasyPrint de forma segura
try:
    from weasyprint import HTML
except (OSError, ImportError) as e:
    HTML = None
    print("Advertencia: WeasyPrint no está instalado o le faltan librerías. Los PDFs no funcionarán en local.")

def factura_pdf(request, venta_id):
    """Genera la factura en PDF."""
    venta = get_object_or_404(Venta, pk=venta_id)
    
    # Si WeasyPrint falló al cargar, devolvemos un error amigable
    if HTML is None:
        return HttpResponse("El servicio de PDF no está disponible localmente (falta WeasyPrint). En Render sí funcionará.", status=503)

    # Renderizar el template HTML de la factura
    html_string = render_to_string('reportes/factura.html', {'venta': venta})
    
    # Generar el PDF
    html = HTML(string=html_string)
    pdf = html.write_pdf()

    # Devolver la respuesta HTTP con el PDF
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="factura_{venta.pk}.pdf"'
    return response