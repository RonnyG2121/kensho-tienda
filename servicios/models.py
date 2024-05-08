from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo = models.CharField(max_length= 50)
    descripcion = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to="servicios") # Este campo permite añadirle imágenes a la base de dato y también permite crear una gerarqía de carpetas para guardar dichas imágenes. esto es en el parámetro
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titulo
    # Creando clase Meta. Donde los metadatos son todos los atributos de la tabla que no son un campo
    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"