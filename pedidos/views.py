from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from carrito.carrito import Carrito
# from pedidos.models import LineaPedido, Pedido
from tienda.models import Producto
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
import stripe


# Create your views here.


def Enviar_mail(*args, **kwargs):
    asunto = "Pedido Realizado con éxito"
    mensaje = render_to_string('emails/pedido.html', {'pedido': kwargs.get(
        "objeto_pedido"), 'lineas_pedido': kwargs.get("lineas_pedido"), 'nombre_usuario': kwargs.get("nombre_usuario")})
    mensaje_texto = strip_tags(mensaje)
    from_email = "omnierfox@gmail.com"
    to_email = kwargs.get('email_usuario')
    send_mail(asunto, mensaje_texto, from_email, [
              to_email], html_message=mensaje, fail_silently=False)


def success(request):
    Enviar_mail()
    # Limpiar el carrito
    if 'carro' in request.session:
        del request.session['carro']
    return render(request, 'pedidos/success.html')


def cancel(request):
    return render(request, 'pedidos/cancel.html')


stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'POST':
        try:
            # Recuperar los datos del carrito del usuario
            # Asegurarse de obtener un diccionario por defecto
            carro = request.session.get('carro', {})
            # print(carrito)

            # Crear los line_items para Stripe
            line_items = [
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': item['nombre'],
                        },
                        'unit_amount': int(float(item['precio']) * 100),
                    },
                    'quantity': item['cantidad'],
                }
                # Iterar sobre los valores del carrito
                for item in carro.values()
            ]

            # Crear la sesión de checkout
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=line_items,
                mode='payment',
                success_url=request.build_absolute_uri(reverse('success')),
                cancel_url=request.build_absolute_uri(reverse('cancel')))

            return JsonResponse({'id': session.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
