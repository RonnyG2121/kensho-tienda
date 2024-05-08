from django.shortcuts import render, redirect
from.forms import Formcontacto
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.


def Contacto(request):
    instancia_contacto_formulario = Formcontacto()
    if request.method == 'POST':
        instancia_contacto_formulario = Formcontacto(data=request.POST)
        if instancia_contacto_formulario.is_valid:
            nombre = request.POST.get('nombre')
            apellido = request.POST.get('apellido')
            email = request.POST.get('email')
            mensaje = request.POST.get('mensaje')
            # Crear el cuerpo del mensaje con la información del formulario
            cuerpo_mensaje = f"{nombre} {apellido} con el correo: {email} te envía lo siguiente:\n\n{mensaje}"
            correo = EmailMessage('Deseo contactarme con la tienda', cuerpo_mensaje, email, [settings.EMAIL_HOST_USER], reply_to=[email])
            try:
                correo.send()
                return redirect('/contacto?valido')
            except:
                return redirect('/contacto?invalido')
            
            # instancia_contacto_formulario.cleaned_data
            return render(request, 'contacto/contacto.html', {'mi_form': instancia_contacto_formulario})
    else:
        instancia_contacto_formulario = Formcontacto()
        return render(request, 'contacto/contacto.html', {'mi_form': Formcontacto})
