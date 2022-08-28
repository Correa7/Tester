from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from Apps.Mascota.views import (
    Editar_Mascota, ficha_mascota, 
    Detail_Mascota, 
    buscar_mascota, lista_mascota,
    Borrar_Mascota 
    )


urlpatterns = [
    path("ficha-mascotas/",ficha_mascota,name="ficha-mascotas"),
    path("buscar-mascota/",buscar_mascota,name="buscar-mascota"),
    path("lista-mascota/", lista_mascota , name="lista-mascota"),
    path("detalle-mascota/<int:pk>/", Detail_Mascota.as_view() , name="detalle-mascota"),
    path("editar-mascota/<int:pk>/", Editar_Mascota.as_view() , name="editar-mascota"),
    path("borrar-mascota/<int:pk>/", Borrar_Mascota.as_view() , name="borrar-mascota"),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
