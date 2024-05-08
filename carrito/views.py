from django.shortcuts import get_object_or_404, redirect

from tienda.models import Producto

from .carrito import Carrito

# Create your views here.


def Agregar_producto(request, producto_id):
    producto_tabla = Producto.objects.get(id=producto_id)
    carro = Carrito(request)
    carro.Agregar(producto=producto_tabla)
    return redirect('tienda')


def Eliminar_producto(request, id_producto):
    carro = Carrito(request)
    mercancia = Producto.objects.get(id=id_producto)
    carro.Eliminar(producto=mercancia)
    return redirect('tienda')


def Restar_producto(request, id_producto):
    carro = Carrito(request)
    mercancia = Producto.objects.get(id=id_producto)
    carro.Restar(producto=mercancia)
    return redirect('tienda')


def Limpia_carro(request, id_producto):
    carro = Carrito(request)
    carro.Limpiar_carro()
    return redirect('tienda')
