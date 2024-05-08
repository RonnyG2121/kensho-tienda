from django.urls import path, include
from .import views


urlpatterns = [
    path('', views.Procesar_pedido, name='pedidos')
]