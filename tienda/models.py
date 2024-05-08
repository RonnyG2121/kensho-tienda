from django.db import models

# Create your models here.

# Creando clase para las categorías de los productos
class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre
    # Clase meta
    class Meta:
        verbose_name = "categoriaproducto"
        verbose_name_plural = "categoriaproductos"

# Creando la clase producto

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categorias = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="tienda", null=True, blank=True)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    # Clase metadata:
    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"

