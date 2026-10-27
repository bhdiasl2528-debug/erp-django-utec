from django.core.management.base import BaseCommand
from productos.models import Producto, Categoria
from decimal import Decimal

class Command(BaseCommand):
    help = 'Carga productos de zapatos reales de prueba en la BD'

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING('\nCargando productos de zapatos...\n'))

        # 0. Desactivar (NO borrar) productos que NO sean zapatos
        nombres_zapatos = ['Air Max Roja', 'Classic Blanca', 'Urban Negra', 'Runner Pro Verde', 'Oxford Café']
        otros = Producto.objects.exclude(nombre__in=nombres_zapatos)
        desactivados = otros.update(activo=False)
        if desactivados > 0:
            self.stdout.write(self.style.SUCCESS(
                f'  [OK] Desactivados {desactivados} productos no-zapato'
            ))

        # 1. Limpieza: renombrar 'Runner Pro Azul' a 'Runner Pro Verde' si existe
        azul = Producto.objects.filter(nombre='Runner Pro Azul').first()
        if azul:
            azul.nombre = 'Runner Pro Verde'
            azul.save()
            self.stdout.write(self.style.SUCCESS(
                '  [OK] Renombrado: Runner Pro Azul -> Runner Pro Verde'
            ))

        # 2. Limpieza: eliminar Laptop de Prueba si existe
        laptops = Producto.objects.filter(nombre__icontains='Laptop')
        if laptops.exists():
            laptops.delete()
            self.stdout.write(self.style.SUCCESS('  [OK] Eliminada: Laptop De Prueba'))

        # 3. Crear categorías si no existen
        cat_sneakers, _ = Categoria.objects.get_or_create(nombre='Sneakers')
        cat_formal, _ = Categoria.objects.get_or_create(nombre='Formal')
        cat_deportivo, _ = Categoria.objects.get_or_create(nombre='Deportivo')

        # 4. Definir los productos
        productos_a_crear = [
            {'nombre': 'Air Max Roja',      'precio': Decimal('2499.00'), 'stock': 15, 'categoria': cat_sneakers},
            {'nombre': 'Classic Blanca',    'precio': Decimal('1899.00'), 'stock': 20, 'categoria': cat_sneakers},
            {'nombre': 'Urban Negra',       'precio': Decimal('3299.00'), 'stock': 8,  'categoria': cat_formal},
            {'nombre': 'Runner Pro Verde',  'precio': Decimal('1599.00'), 'stock': 30, 'categoria': cat_deportivo},
            {'nombre': 'Oxford Café',       'precio': Decimal('2799.00'), 'stock': 5,  'categoria': cat_formal},
        ]

        creados = 0
        for p_data in productos_a_crear:
            prod, created = Producto.objects.get_or_create(
                nombre=p_data['nombre'],
                defaults={
                    'precio': p_data['precio'],
                    'stock': p_data['stock'],
                    'categoria': p_data['categoria'],
                    'activo': True,
                }
            )
            if created:
                creados += 1
                self.stdout.write(self.style.SUCCESS(
                    f'  [OK] Creado: {prod.nombre} (${prod.precio})'
                ))
            else:
                self.stdout.write(self.style.WARNING(f'  [INFO] Ya existía: {prod.nombre}'))

        self.stdout.write(self.style.SUCCESS(
            f'\n[OK] {creados} productos nuevos cargados exitosamente.\n'
        ))