from django.contrib import admin
from .models import Servicio
# Register your models here.
# Creando clase para mostrar el campo hora de creación y actualización en el panel de administración
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

# Registrando el servicio:
admin.site.register(Servicio, ServicioAdmin)
