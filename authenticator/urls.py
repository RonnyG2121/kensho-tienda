from django.urls import path, include
from .import views
from .views import VistaRegistro


urlpatterns = [
    path('', VistaRegistro.as_view(), name='authenticator'),
    path('logout/', views.CerrarSesion, name='logout'),
    path('login/', views.Login, name='login'),

]