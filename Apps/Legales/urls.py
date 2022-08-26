from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Apps.Legales.views import preg_frecuentes,terminos,privacidad

urlpatterns = [
    path("preguntas-frecuentes/",preg_frecuentes,name="preguntas-frecuentes"),
    path("terminos-condiciones/",terminos,name="terminos-condiciones"),
    path("politica-privacidad/",privacidad,name="politica-privacidad")
    ]