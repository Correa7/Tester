from django.urls import path
from Apps.Mascota.views import ficha_mascota, busqueda_mascota, buscar_mascota

urlpatterns = [
    path("ficha-mascotas/",ficha_mascota,name="ficha-mascotas"),
    path("ficha-busqueda-mascota/", busqueda_mascota, name="ficha-busqueda-mascota"),
    path("buscar-mascota/",buscar_mascota,name="buscar-mascota"),
    
]
