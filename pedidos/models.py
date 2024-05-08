from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import F, FloatField, Sum

from tienda.models import Producto

user = get_user_model()

# Create your models here.


class Pedido(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    created_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

    @property
    def Total(self):
        return self.LineaPedido_set.aggregate(total=Sum(F('precio') * F('cantidad'), output_field=FloatField()))['total'] or 0.0

    class Meta:
        db_table = "pedidos"
        verbose_name = "pedido"
        verbose_name_plural = "pedidos"
        ordering = ['id']


class LineaPedido(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} unidades de {}".format(self.cantidad, self.producto.nombre)

    class Meta:
        db_table = "linea_pedidos"
        verbose_name = "linea_pedido"
        verbose_name_plural = "lineas_pedidos"
        ordering = ['id']
