from django.shortcuts import render
from blog.models import Post, Categoria
# Create your views here.
def Blog(request):
    muestra_blog = Post.objects.all()
    return render(request, 'blog/blog.html', {'clabe_blog': muestra_blog})

def Categoria_funcion(request, categoria_id):
    filtra_categoria = Categoria.objects.get(id=categoria_id)
    filtra_post = Post.objects.filter(categorias=filtra_categoria)
    return render(request, 'blog/categoria.html', {'clabe_categoria': filtra_categoria, 'clabe_blog': filtra_post})
