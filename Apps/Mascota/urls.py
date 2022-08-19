from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Apps.Mascota.views import ficha_mascota, busqueda_mascota, buscar_mascota, lista_mascota 

urlpatterns = [
    path("ficha-mascotas/",ficha_mascota,name="ficha-mascotas"),
    path("ficha-busqueda-mascota/", busqueda_mascota, name="ficha-busqueda-mascota"),
    path("buscar-mascota/",buscar_mascota,name="buscar-mascota"),
    path("lista-mascota/", lista_mascota , name="lista-mascota"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
