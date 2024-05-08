from django.contrib import admin
from .models import Categoria, Post
# Register your models here.
class AdminCategoria(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class AdminPost(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

# Registrando estas cclases en el panel de administración

admin.site.register(Categoria, AdminCategoria)
admin.site.register(Post, AdminPost)