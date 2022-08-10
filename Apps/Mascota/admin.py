from django.contrib import admin
from Apps.Mascota.models import  Mascota
# Register your models here.


class Mascota_admin(admin.ModelAdmin):
    list_display = ["nickname","especie","raza","sexo","edad_aprox","ingreso"]

admin.site.register(Mascota,Mascota_admin)