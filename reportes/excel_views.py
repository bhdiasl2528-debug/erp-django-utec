# reportes/excel_views.py
"""Exportación a Excel — W12.

Usa openpyxl para generar un archivo .xlsx con el inventario
de productos.
"""
from io import BytesIO

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

from productos.models import Producto


@login_required
def productos_excel(request):
    """Genera y devuelve un Excel con el inventario de productos."""
    # 1. Crear el libro de Excel
    wb = Workbook()
    ws = wb.active
    ws.title = 'Inventario'

    # 2. Encabezados con estilo
    headers = ['ID', 'Nombre', 'Categoría', 'Proveedor',
               'Precio', 'Stock', 'Activo']
    ws.append(headers)

    header_font = Font(bold=True, color='FFFFFF', size=12)
    header_fill = PatternFill(
        start_color='0A0A0A', end_color='0A0A0A', fill_type='solid'
    )
    header_align = Alignment(horizontal='center', vertical='center')

    for cell in ws[1]:
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = header_align

    # 3. Datos
    for p in Producto.objects.select_related('categoria', 'proveedor').all():
        ws.append([
            p.pk,
            p.nombre,
            p.categoria.nombre if p.categoria else '',
            p.proveedor.nombre if p.proveedor else '—',
            float(p.precio),
            p.stock,
            'Sí' if p.activo else 'No',
        ])

    # 4. Ajustar el ancho de las columnas
    columnas_anchas = {
        'A': 8, 'B': 30, 'C': 20, 'D': 25, 'E': 12, 'F': 10, 'G': 10
    }
    for letra, ancho in columnas_anchas.items():
        ws.column_dimensions[letra].width = ancho

    # 5. Guardar en memoria
    buffer = BytesIO()
    wb.save(buffer)
    buffer.seek(0)

    # 6. Devolver como descarga
    response = HttpResponse(
        buffer.getvalue(),
        content_type=(
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        ),
    )
    response['Content-Disposition'] = (
        'attachment; filename="inventario_dl_shoes.xlsx"'
    )
    return response