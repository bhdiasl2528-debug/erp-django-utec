# productos/validators.py
"""Validadores de archivos de imagen para la app productos — W11."""
import filetype
from PIL import Image, UnidentifiedImageError

from django.core.exceptions import ValidationError


MAX_IMAGE_SIZE = 5 * 1024 * 1024   # 5 MB

FORMATOS_MIME_PERMITIDOS   = {'image/jpeg', 'image/png', 'image/webp'}
FORMATOS_PILLOW_PERMITIDOS = {'JPEG', 'PNG', 'WEBP'}


def validar_imagen_producto(archivo) -> None:
    """Valida un archivo subido como imagen de producto."""
    # 1. Tamaño
    if archivo.size > MAX_IMAGE_SIZE:
        raise ValidationError(
            f'La imagen supera el tamaño máximo permitido de 5 MB. '
            f'Tamaño recibido: {archivo.size / (1024 * 1024):.1f} MB.'
        )

    # 2. MIME real
    archivo.seek(0)
    cabecera = archivo.read(512)
    archivo.seek(0)
    tipo = filetype.guess(cabecera)
    if tipo is None or tipo.mime not in FORMATOS_MIME_PERMITIDOS:
        mime = tipo.mime if tipo else 'desconocido'
        raise ValidationError(
            f'Tipo de archivo no permitido: {mime}. '
            f'Solo se aceptan: JPEG, PNG, WEBP.'
        )

    # 3. Pillow
    archivo.seek(0)
    try:
        img = Image.open(archivo)
        img.verify()
    except (UnidentifiedImageError, Exception) as exc:
        raise ValidationError(
            f'El archivo no es una imagen válida o está corrupto: {exc}'
        )
    finally:
        archivo.seek(0)