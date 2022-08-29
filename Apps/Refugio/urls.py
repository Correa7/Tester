from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import (
                    Ficha_refugio, buscar_refugio,
                    Detail_Refugio, lista_refugio, create_perfil_refugio,
                    Editar_Refugio_Perfil, show_perfil_refugio,
                    Borrar_Refugio_Perfil, Borrar_Refugio, Editar_Refugio
                    )


urlpatterns = [
    path("ficha-refugio/", Ficha_refugio, name="ficha-refugio"),
    path("editar-refugio/<int:pk>/", Editar_Refugio.as_view() , name="editar-refugio"),
    path("borrar-refugio/<int:pk>/", Borrar_Refugio.as_view() , name="borrar-refugio"),
    path("buscar-refugio/", buscar_refugio, name="buscar-refugio"), 
    path("lista-refugio/", lista_refugio , name="lista-refugio"),
    path("detalle-refugio/<int:pk>/", Detail_Refugio.as_view() , name="detalle-refugio"),
    path("perfil-refugio/", show_perfil_refugio , name="perfil-refugio"),
    path('crear-profile-refugio/<int:id>/', create_perfil_refugio, name='crear-profile-refugio'),
   path("editar-refugio-perfil/<int:pk>/", Editar_Refugio_Perfil.as_view() , name="editar-refugio-perfil"),
    path("borrar-refugio-perfil/<int:pk>/", Borrar_Refugio_Perfil.as_view() , name="borrar-refugio-perfil"),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
