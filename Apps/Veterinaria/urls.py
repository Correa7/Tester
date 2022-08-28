from django.urls import path
from Apps.Veterinaria.views import (
    Ficha_veterinaria, buscar_ficha, 
    busqueda_Vacuna, lista_fichas,
    Editar_Vacuna,Borrar_Vacuna

    )
    
urlpatterns = [
    path("ficha-veterinaria/<int:pk>", Ficha_veterinaria, name="ficha-veterinaria"),
    path("ficha-busqueda/", busqueda_Vacuna, name="ficha-busqueda"),
    path("buscar/", buscar_ficha, name="buscar"),
    path("lista/", lista_fichas ,name="lista"),
    path("editar-vacuna/<int:pk>/", Editar_Vacuna.as_view() , name="editar-vacuna"),
    path("borrar-vacuna/<int:pk>/", Borrar_Vacuna.as_view() , name="borrar-vacuna"),
    ]
