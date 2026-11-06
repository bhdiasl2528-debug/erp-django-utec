from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = 'Crea los grupos de usuarios y les asigna permisos'

    def handle(self, *args, **kwargs):
        # Creamos todos los grupos que el sistema necesita
        grupos = ['Administrador', 'Gerente', 'Vendedor', 'Almacen', 'Cajero']
        
        for nombre in grupos:
            Group.objects.get_or_create(name=nombre)
            
        self.stdout.write(self.style.SUCCESS('Grupos creados exitosamente.'))