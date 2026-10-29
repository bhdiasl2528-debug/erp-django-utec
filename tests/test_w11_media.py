"""Suite de pruebas W11 — ImageField, validadores y API media."""
import io
import os

from decimal import Decimal
from PIL import Image

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

from productos.models     import Categoria, Producto
from productos.validators import validar_imagen_producto


def _imagen(nombre='img.jpg', formato='JPEG', content_type='image/jpeg',
            size=(100, 100)) -> SimpleUploadedFile:
    buf = io.BytesIO()
    Image.new('RGB', size, color='teal').save(buf, format=formato)
    buf.seek(0)
    return SimpleUploadedFile(nombre, buf.read(), content_type=content_type)


def _archivo_invalido() -> SimpleUploadedFile:
    return SimpleUploadedFile(
        'notimage.exe',
        b'\x00\x01fake binary content\xff\xfe',
        content_type='application/octet-stream'
    )


class ValidadorImagenTest(TestCase):
    """Tests del validador validar_imagen_producto."""

    def test_imagen_jpeg_valida_pasa(self):
        archivo = _imagen()
        try:
            validar_imagen_producto(archivo)
        except ValidationError as e:
            self.fail(f"Imagen JPEG válida lanzó ValidationError: {e}")

    def test_imagen_png_valida_pasa(self):
        archivo = _imagen('img.png', 'PNG', 'image/png')
        try:
            validar_imagen_producto(archivo)
        except ValidationError as e:
            self.fail(f"Imagen PNG válida lanzó ValidationError: {e}")

    def test_archivo_no_imagen_lanza_error(self):
        archivo = _archivo_invalido()
        with self.assertRaises(ValidationError) as ctx:
            validar_imagen_producto(archivo)
        self.assertIn('no permitido', str(ctx.exception).lower())

    def test_imagen_muy_grande_lanza_error(self):
        archivo = _imagen()
        archivo.size = 6 * 1024 * 1024
        with self.assertRaises(ValidationError) as ctx:
            validar_imagen_producto(archivo)
        self.assertIn('5 mb', str(ctx.exception).lower())


class ProductoImagenModelTest(TestCase):
    """Tests del ImageField en el modelo Producto."""

    def setUp(self):
        self.cat = Categoria.objects.create(nombre='Cat Media')

    def tearDown(self):
        for prod in Producto.objects.all():
            if prod.imagen:
                try:
                    os.remove(prod.imagen.path)
                except FileNotFoundError:
                    pass

    def test_producto_sin_imagen_es_valido(self):
        prod = Producto.objects.create(
            nombre='Sin imagen', precio=Decimal('100.00'),
            stock=5, categoria=self.cat
        )
        self.assertFalse(bool(prod.imagen))

    def test_producto_puede_guardarse_con_imagen(self):
        prod = Producto(
            nombre='Con imagen', precio=Decimal('200.00'),
            stock=3, categoria=self.cat,
            imagen=_imagen()
        )
        prod.save()
        self.assertTrue(bool(prod.imagen))
        self.assertIn('productos/', prod.imagen.name)


class ProductoAPIImagenTest(APITestCase):
    """Tests del campo imagen_url en la API."""

    def setUp(self):
        self.client = APIClient()
        self.user   = User.objects.create_user('mediauser', password='pass')
        self.token  = Token.objects.create(user=self.user)
        self.cat    = Categoria.objects.create(nombre='Cat API')

    def tearDown(self):
        for prod in Producto.objects.all():
            if prod.imagen:
                try:
                    os.remove(prod.imagen.path)
                except FileNotFoundError:
                    pass

    def test_api_devuelve_imagen_url_none_sin_imagen(self):
        prod = Producto.objects.create(
            nombre='Sin img API', precio=Decimal('100.00'),
            stock=5, categoria=self.cat
        )
        r = self.client.get(f'/api/productos/{prod.pk}/')
        self.assertEqual(r.status_code, 200)
        self.assertIsNone(r.json().get('imagen_url'))

    def test_api_devuelve_imagen_url_con_imagen(self):
        prod = Producto(
            nombre='Con img API', precio=Decimal('300.00'),
            stock=2, categoria=self.cat,
            imagen=_imagen()
        )
        prod.save()
        r = self.client.get(f'/api/productos/{prod.pk}/')
        self.assertEqual(r.status_code, 200)
        url = r.json().get('imagen_url')
        self.assertIsNotNone(url)
        self.assertIn('productos/', url)