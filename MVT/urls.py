from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from MVT.views import index, padre, inicio, en_construccion, voluntarios

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("padre/", padre, name="padre"),
    path("inicio/", inicio, name="inicio"),
    path("en-construccion/", en_construccion, name="en_construccion"),
    path("voluntarios/", voluntarios, name="voluntarios"),
    path("Mascota/", include("Apps.Mascota.urls")),
    path("Refugio/", include("Apps.Refugio.urls")),
    path("Veterinaria/", include("Apps.Veterinaria.urls")),
    path("User/", include("Apps.User.urls")),
    path("SendMail/", include("Apps.SendMail.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)