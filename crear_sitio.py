import os
import django

# Configurar Django para que use settings_prod
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings_prod')
django.setup()

from django.contrib.sites.models import Site

# Crear el sitio si no existe
site, created = Site.objects.get_or_create(
    id=1,
    defaults={
        'domain': 'erp-django-utec-y4xg.onrender.com',
        'name': 'DL Shoes ERP'
    }
)
if created:
    print(f"[OK] Sitio creado: {site.domain}")
else:
    print(f"[INFO] El sitio ya existe: {site.domain}")