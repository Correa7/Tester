from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import (form_newsletter, form_voluntario, form_adopcion, form_donar)

urlpatterns = [
    path("adopcion/", form_adopcion, name="adopcion"),
    path("voluntario/", form_voluntario, name="voluntario"),
    path("donaciones/", form_donar, name="donaciones"),
    path("news-letter/", form_newsletter, name="news-letter"),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)