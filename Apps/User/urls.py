from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Apps.User.views import  login_view,logout_view, register_view,create_perfil, \
     show_perfil,  edit_perfil, eliminar_perfil, edit_user, del_user


urlpatterns = [   
    path("perfil", show_perfil , name="perfil"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('eliminar-usuario/<int:id>/', del_user, name='eliminar-usuario'),
    path('edit-usuario/<int:id>', edit_user, name='edit-user'),
    path('crear-profile/', create_perfil, name='crear-profile'),
    path('edit-profile/<int:id>', edit_perfil, name='edit-profile'),
    path('eliminar-profile/<int:id>/', eliminar_perfil, name='eliminar-profile'),    
    ]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
