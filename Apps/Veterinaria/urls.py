from django.urls import path
from Apps.Veterinaria.views import Ficha_veterinaria, buscar_ficha, busqueda_Vacuna, lista_fichas
    
urlpatterns = [
    path("ficha-veterinaria/", Ficha_veterinaria, name="ficha-veterinaria"),
    path("ficha-busqueda/", busqueda_Vacuna, name="ficha-busqueda"),
    path("buscar/", buscar_ficha, name="buscar"),
    path("lista/", lista_fichas ,name="lista"),
    ]
