from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from MVT.views import form_index, padre, inicio, en_construccion, about, presentacion, voluntarios


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", form_index, name="index"),
    path("admin/", admin.site.urls),
   
    path("padre/", padre, name="padre"),
    path("inicio/", inicio, name="inicio"),
    path("en-construccion/", en_construccion, name="en_construccion"),
    path("about/", about, name="about"),
    path("voluntarios/", voluntarios, name="voluntarios"),
    path("presentacion/", presentacion, name="presentacion"),
    path("Mascota/", include("Apps.Mascota.urls")),
    path("Refugio/", include("Apps.Refugio.urls")),
    path("Veterinaria/", include("Apps.Veterinaria.urls")),
    path("User/", include("Apps.User.urls")),
    path("SendMail/", include("Apps.SendMail.urls")),
    path("Legales/",include("Apps.Legales.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)