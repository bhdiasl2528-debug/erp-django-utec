# productos/urls.py
"""URLs de la app productos — W07 (Lista + Detalle)."""
from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('',
         views.ProductoListView.as_view(),
         name='lista'),
    path('<int:producto_id>/',
         views.ProductoDetailView.as_view(),
         name='detalle'),
]