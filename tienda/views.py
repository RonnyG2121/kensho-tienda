from django.shortcuts import render
from .models import Producto, CategoriaProducto
from django.conf import settings
# Create your views here.
STRIPE_PUBLIC_KEY = settings.STRIPE_PUBLIC_KEY
def Tienda(request):
    muestra_producto = Producto.objects.all()
    return render(request, 'tienda/tienda.html', {'clave_producto': muestra_producto, 'STRIPE_PUBLIC_KEY': STRIPE_PUBLIC_KEY})
