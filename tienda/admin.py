from django.contrib import admin
from .models import CategoriaProducto, Producto
# Register your models here.
# Creando las clases de administración para poder manejar dentro del panel de control de la página

class AdminCategoria(admin.ModelAdmin):
    readonly_fields = "created", "updated"


class AdminProducto(admin.ModelAdmin):
    readonly_fields = "created", "updated"
    

# Registrando estos modelos
admin.site.register(CategoriaProducto, AdminCategoria)
admin.site.register(Producto, AdminProducto)
