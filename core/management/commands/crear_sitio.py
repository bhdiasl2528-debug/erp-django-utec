from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Crea el sitio con ID=1 en la base de datos si no existe'

    def handle(self, *args, **options):
        site, created = Site.objects.get_or_create(
            id=1,
            defaults={
                'domain': 'erp-django-utec-y4xg.onrender.com',
                'name': 'DL Shoes ERP'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'[OK] Sitio creado: {site.domain}'))
        else:
            self.stdout.write(self.style.SUCCESS(f'[INFO] El sitio ya existe: {site.domain}'))