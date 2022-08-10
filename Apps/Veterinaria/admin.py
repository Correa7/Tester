from django.contrib import admin
from Apps.Veterinaria.models import  Ficha_medica
# Register your models here.



class Ficha_admin(admin.ModelAdmin):
    list_display = ["registro","vacuna_1","vacuna_2","desparasitacion","castracion", "observaciones"]



# admin.site.register(Usuario, Usuario_admin)

admin.site.register(Ficha_medica, Ficha_admin)
