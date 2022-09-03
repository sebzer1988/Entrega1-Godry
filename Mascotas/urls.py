from django.urls import path
from Mascotas.views import *

urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    path("perros/", perros, name="perros"),
    path("gatos/", gatos, name="gatos"),
    path("animales/", animales, name="animales"),
    path("busquedaPerro/", busquedaPerro, name="busquedaPerro"),
    path("buscar/", buscar, name="buscar"),
]