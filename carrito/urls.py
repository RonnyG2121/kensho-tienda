from django.urls import path, include
from .import views

app_name = 'carro'

urlpatterns = [
    path('agregar/<int:producto_id>/', views.Agregar_producto, name='agregar'),
    path('eliminar/<int:id_producto>/', views.Eliminar_producto, name='aliminar'),
    path('restar/<int:id_producto>/', views.Restar_producto, name='restar'),
    path('limpiar/', views.Limpia_carro, name='limpiar'),    

]