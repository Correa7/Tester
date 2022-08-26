from django.contrib import admin
from Apps.Refugio.models import Refugio, Perfil_Refugio

class Refugio_admin(admin.ModelAdmin):
    list_display = ["nombre","telefono","email","domicilio"]

admin.site.register(Refugio, Refugio_admin)


class Perfil_Refugio_admin(admin.ModelAdmin):
    list_display = ["description","image_1","image_2","image_3","image_4",]

admin.site.register(Perfil_Refugio, Perfil_Refugio_admin)   