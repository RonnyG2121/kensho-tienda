from django.shortcuts import render
from .models import Producto, CategoriaProducto
# Create your views here.

def Tienda(request):
    muestra_producto = Producto.objects.all()
    return render(request, 'tienda/tienda.html', {'clave_producto': muestra_producto})
