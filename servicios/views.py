from django.shortcuts import render
from servicios.models import Servicio

# Create your views here.
def Servicios(request):
    muestra_servicios = Servicio.objects.all()
    return render(request, 'servicios/servicios.html', {'clabe_servicios': muestra_servicios})

