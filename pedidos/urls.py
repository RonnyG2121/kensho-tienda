from django.urls import include, path

from .views import *

urlpatterns = [
    path('', Procesar_pedido, name='pedidos'),
    path('', pagar, name='pagar'),
]
