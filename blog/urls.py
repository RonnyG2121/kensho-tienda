from django.urls import path, include
from .import views


urlpatterns = [
    path('', views.Blog, name='blog'),
    path('categoria/<int:categoria_id>/', views.Categoria_funcion, name='categoria')

]