import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from carrito.carrito import Carrito
from pedidos.models import LineaPedido, Pedido
from tienda.models import Producto

from .forms import PaymentForm

# Create your views here.


def pagar(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    if request.method == "POST":
        formulario_pago = PaymentForm(request.POST)
        if formulario_pago.is_valid():
            token = request.POST['stripeToken']

            try:
                charge_customer = stripe.Charge.create(
                    amount=1000,
                    currency='eur',
                    description='Ejemplo de carga',
                    source=token)

                return redirect('tienda')

            except stripe.error.CardError as e:
                error_message = e.error.message
                return render(request, "pedidos/form_pago.html", {"formulario_pago": formulario_pago, "error_message": error_message})
    else:
        formulario_pago = PaymentForm()
        return render(request, "pedidos/form_pago.html", {'formulario_pago': formulario_pago})


def Enviar_mail(*args, **kwargs):
    asunto = "Pedido Realizado con éxito"
    mensaje = render_to_string('emails/pedido.html', {'pedido': kwargs.get(
        "objeto_pedido"), 'lineas_pedido': kwargs.get("lineas_pedido"), 'nombre_usuario': kwargs.get("nombre_usuario")})
    mensaje_texto = strip_tags(mensaje)
    from_email = "omnierfox@gmail.com"
    to_email = kwargs.get('email_usuario')
    send_mail(asunto, mensaje_texto, from_email, [
              to_email], html_message=mensaje, fail_silently=False)


@login_required(login_url='authenticator/login')
def Procesar_pedido(request):
    objeto_pedido = Pedido.objects.create(user=request.user)
    carro = Carrito(request)
    lineas_pedido = list()
    for key, value in carro.carro.items():
        producto = get_object_or_404(Producto, pk=key)
        lineas_pedido.append(LineaPedido(
            producto=producto,
            cantidad=value['cantidad'],
            user=request.user,
            pedido=objeto_pedido))
    LineaPedido.objects.bulk_create(lineas_pedido)
    """Enviar_mail(objeto_pedido=objeto_pedido, lineas_pedido=lineas_pedido, nombre_usuario=request.user.username, email_usuario=request.user.email)"""
    messages.success(
        request, '¡Exito! Su pedido se efectuó satisfactoriamente')
    carro.Limpiar_carro()
    pagar(request)
    return redirect('tienda')
