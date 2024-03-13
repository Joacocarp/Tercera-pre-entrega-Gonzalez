from django.urls import path, include
from .views import * 

urlpatterns = [
    path('', home, name = "home"), 
    path('remeras/', remeras, name = "remeras"),
    path('pantalones/', pantalones, name = "pantalones"),
    path('buzos/', buzos, name = "buzos"),
    path('clientes/', clientes, name = "clientes"),
    path('acerca/', acerca, name = "acerca_de_mi"),
    path('agregar_cliente/', agregar_cliente, name = "agregar_cliente"),
    path('agregar_remera/', agregar_remera, name = "agregar_remera"),
    
    path('cliente_form/', clienteForm, name = "cliente_form"),
    path('remera_form/', remeraForm, name = "remera_form"),
    path('pantalon_form/', pantalonForm, name = "pantalon_form"),
    path('buzo_form/', buzoForm, name = "buzo_form"),

    path('buscar_articulo/', buscar, name = "buscar_articulo"),
    path('encontrar_articulo/', encontrarArticulo, name = "encontrar_articulo"),
]


