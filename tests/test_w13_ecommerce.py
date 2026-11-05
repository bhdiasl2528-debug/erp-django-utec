"""Suite de pruebas W13 — Catálogo público y carrito de compras."""
from decimal import Decimal
from django.test import TestCase
from django.urls import reverse
from productos.models import Categoria, Producto

class CatalogoPublicoTest(TestCase):
    def setUp(self):
        cat = Categoria.objects.create(nombre='Electrónica')
        self.prod1 = Producto.objects.create(nombre='Laptop', precio=Decimal('10000.00'), stock=5, categoria=cat)
        self.prod2 = Producto.objects.create(nombre='Mouse', precio=Decimal('250.00'), stock=20, categoria=cat)
        Producto.objects.create(nombre='Producto Inactivo', precio=Decimal('100.00'), stock=5, categoria=cat, activo=False)

    def test_catalogo_accesible_sin_auth(self):
        r = self.client.get(reverse('catalogo:catalogo'))
        self.assertEqual(r.status_code, 200)

    def test_catalogo_solo_muestra_activos(self):
        r = self.client.get(reverse('catalogo:catalogo'))
        nombres = [p.nombre for p in r.context['productos']]
        self.assertIn('Laptop', nombres)
        self.assertNotIn('Producto Inactivo', nombres)

    def test_catalogo_filtro_por_nombre(self):
        r = self.client.get(reverse('catalogo:catalogo'), {'nombre': 'lapt'})
        self.assertEqual(r.status_code, 200)
        nombres = [p.nombre for p in r.context['productos']]
        self.assertIn('Laptop', nombres)
        self.assertNotIn('Mouse', nombres)

    def test_catalogo_filtro_por_precio_max(self):
        r = self.client.get(reverse('catalogo:catalogo'), {'precio_max': 500})
        nombres = [p.nombre for p in r.context['productos']]
        self.assertIn('Mouse', nombres)
        self.assertNotIn('Laptop', nombres)

class CarritoTest(TestCase):
    def setUp(self):
        cat = Categoria.objects.create(nombre='Cat')
        self.prod = Producto.objects.create(nombre='Teclado', precio=Decimal('350.00'), stock=10, categoria=cat)

    def test_carrito_vacio_al_inicio(self):
        r = self.client.get(reverse('catalogo:carrito'))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.context['items'], [])

    def test_agregar_producto_incrementa_carrito(self):
        self.client.post(reverse('catalogo:agregar', args=[self.prod.pk]), {'cantidad': 2})
        r = self.client.get(reverse('catalogo:carrito'))
        self.assertEqual(len(r.context['items']), 1)
        self.assertEqual(r.context['items'][0]['cantidad'], 2)

    def test_agregar_mismo_producto_acumula_cantidad(self):
        url = reverse('catalogo:agregar', args=[self.prod.pk])
        self.client.post(url, {'cantidad': 1})
        self.client.post(url, {'cantidad': 3})
        r = self.client.get(reverse('catalogo:carrito'))
        self.assertEqual(r.context['items'][0]['cantidad'], 4)

    def test_carrito_calcula_total_correcto(self):
        self.client.post(reverse('catalogo:agregar', args=[self.prod.pk]), {'cantidad': 2})
        r = self.client.get(reverse('catalogo:carrito'))
        self.assertEqual(r.context['total'], Decimal('700.00'))

    def test_remover_producto_lo_elimina(self):
        self.client.post(reverse('catalogo:agregar', args=[self.prod.pk]), {'cantidad': 1})
        self.client.post(reverse('catalogo:remover', args=[self.prod.pk]))
        r = self.client.get(reverse('catalogo:carrito'))
        self.assertEqual(r.context['items'], [])