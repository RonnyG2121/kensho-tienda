from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.

# Crearé una clase para manejar el formulario de autenticación usaré la clase userCreationForm

class VistaRegistro(View):
    def get(self, request):
# instancia de la clase UserCreationForm
        form = UserCreationForm()
        return render(request, 'authenticator/registro.html', {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request=request, user=usuario)
            return redirect('inicio')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, 'authenticator/registro.html', {"form": form})


def CerrarSesion(request):
    logout(request)
    return redirect('inicio')

def Login(request):
    form_login = AuthenticationForm()
    if request.method == 'POST':
        form_login = AuthenticationForm(request, data=request.POST)
        if form_login.is_valid():
            nombre_usuario = form_login.cleaned_data.get('username')
            contraseña = form_login.cleaned_data.get('password')
            usuario = authenticate(request, username=nombre_usuario, password=contraseña)
            if usuario is not None:
                login(request, usuario)
                return redirect('inicio')
            else:
                messages.error(request, message='Los datos ingresados no son correctos. Por favor inténtelo de nuevo')
        else:
            messages.error(request, message='Los datos ingresados no son correctos. Por favor inténtelo de nuevo')
    return render(request, 'login/login.html', {'form_login': form_login})

