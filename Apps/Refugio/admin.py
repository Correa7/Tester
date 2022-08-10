from django.contrib import admin
from Apps.Refugio.models import Refugio
# Register your models here.

class Refugio_admin(admin.ModelAdmin):
    list_display = ["nombre","telefono","email","domicilio"]

admin.site.register(Refugio, Refugio_admin)   