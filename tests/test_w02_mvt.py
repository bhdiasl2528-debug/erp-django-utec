"""Suite de pruebas W02 — MVT y templates básicos (Actualizado en W07)."""
from django.test import TestCase
from django.urls import reverse


class TemplatesRenderTest(TestCase):
    """Verifica que las vistas usan los templates correctos."""

    def test_bienvenida_usa_template_correcto(self):
        """La vista de inicio debe renderizar index.html."""
        # Usamos '/' directo para no depender del nombre de la ruta en core/urls.py
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_productos_usa_template_correcto(self):
        """La vista de productos debe usar productos/lista.html."""
        response = self.client.get(reverse('productos:lista'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'productos/lista.html')

    def test_clientes_usa_template_correcto(self):
        """La vista de clientes debe usar clientes/lista.html."""
        response = self.client.get(reverse('clientes:lista'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'clientes/lista.html')

    def test_proveedores_usa_template_correcto(self):
        """La vista de proveedores debe usar proveedores/lista.html."""
        response = self.client.get(reverse('proveedores:lista'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'proveedores/lista.html')

    def test_ventas_usa_template_correcto(self):
        """La vista de ventas debe usar ventas/lista.html."""
        response = self.client.get(reverse('ventas:lista'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ventas/lista.html')