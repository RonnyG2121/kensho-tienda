from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length= 50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
# función string que devuelve el nombre
    def __str__(self):
        return self.nombre
# Clase metadata
    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"


class Post(models.Model):
    titulo = models.CharField(max_length= 50)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to="blog", null=True, blank=True) # Este campo permite añadirle imágenes a la base de datos y también permite crear una gerarqía de carpetas para guardar dichas imágenes y permite que añadir una imagen sea opcional
    autor = models.ForeignKey(User, on_delete=models.CASCADE) # Este campo crea una relación usuario/post si se elimina un usuario, también se eliminarán sus posts
    categorias = models.ManyToManyField(Categoria) # Esto crea una relación post/categoría y viceverza
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
# función string que devuelve el nombre
    def __str__(self):
        return self.titulo

# Clase metadata
    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"