from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import (
                    Ficha_refugio, busqueda_refugio, buscar_refugio,
                    Detail_Refugio, lista_refugio, create_perfil_refugio,
                    edit_perfil_refugio, show_perfil_refugio,
                    eliminar_perfil_refugio
                    )


urlpatterns = [
    path("ficha-refugio/", Ficha_refugio, name="ficha-refugio"),
    path("ficha-busqueda-refugio/", busqueda_refugio, name="ficha-busqueda-refugio"),
    path("buscar-refugio/", buscar_refugio, name="buscar-refugio"), 
    path("lista-refugio/", lista_refugio , name="lista-refugio"),
    path("detalle-refugio/<int:pk>/", Detail_Refugio.as_view() , name="detalle-refugio"),
    path("perfil-refugio", show_perfil_refugio , name="perfil-refugio"),
    path('crear-profile-refugio/', create_perfil_refugio, name='crear-profile-refugio'),
    path('edit-profile-refugio/<int:id>', edit_perfil_refugio, name='edit-profile-refugio'),
    path('eliminar-profile-refugio/<int:id>/', eliminar_perfil_refugio, name='eliminar-profile-refugio'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
