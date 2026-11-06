from django import template

register = template.Library()

@register.filter
def limpiar_ruta(value):
    if not value:
        return ""
    # Reemplaza las diagonales invertidas de Windows por diagonales normales
    return str(value).replace("\\", "/")