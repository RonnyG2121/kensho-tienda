from django.contrib import admin
from .models import Pedido, LineaPedido

# Register your models here.
# Registrando las tablas de los pedidos en el panel de administración

class AdminPedido(admin.ModelAdmin):
    readonly_fields = ("created_add",)

# Registrando
admin.site.register(Pedido, AdminPedido)

class AdminLineaPedido(admin.ModelAdmin):
    readonly_fields = ("created_add",)

# Registrando
admin.site.register(LineaPedido, AdminLineaPedido)
