from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from Apps.User.views import  login_view,logout_view, register_view,create_perfil, \
     respuesta,show_perfil,  edit_perfil, eliminar_profile

urlpatterns = [

    # path("", index, name="index"),
    # path("padre/", padre, name="padre"),
    # path("inicio/", inicio, name="inicio"),
    # path("en-construccion/", en_construccion, name="en_construccion"),
    path("respuesta/", respuesta, name="respuesta"),
    path("perfil", show_perfil , name="perfil"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('crear-profile/', create_perfil, name='crear-profile'),
    path('edit-profile/<int:id>', edit_perfil, name='edit-profile'),
    path('eliminar-profile/<int:id>/', eliminar_profile, name='eliminar-profile'),
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
