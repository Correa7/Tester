from django.urls import path

from Apps.Refugio.views import Ficha_refugio, busqueda_refugio, buscar_refugio

urlpatterns = [
    
    path("ficha-refugio/", Ficha_refugio, name="ficha-refugio"),
    path("ficha-busqueda-refugio/", busqueda_refugio, name="ficha-busqueda-refugio"),
    path("buscar-refugio/", buscar_refugio, name="buscar-refugio"), 
      
]
