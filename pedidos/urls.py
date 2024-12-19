from django.urls import include, path

from .views import *

urlpatterns = [
    path('create-checkout-session/', create_checkout_session, name='create-checkout-session'),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel'),


]
