from django.db import models
from Apps.Mascota.models import Mascota

class Ficha_medica (models.Model):
    mascota = models.OneToOneField(Mascota, on_delete=models.CASCADE, related_name='veterinaria', null=True)
    registro = models.IntegerField(unique=True)
    vacuna_1 = models.CharField(max_length= 100, null=True, blank=True,)
    vacuna_2 = models.CharField(max_length= 100, null=True, blank=True,)
    desparasitacion = models.CharField(max_length=50, null=True, blank=True,)
    castracion = models.CharField(max_length=50, null=True, blank=True,)
    observaciones = models.TextField(max_length=150,null=True, blank=True,)

    def __str__(self) -> str:
        return f" {self.registro} - {self.vacuna_1} - {self.vacuna_2} - {self.desparasitacion} - {self.castracion} - {self.observaciones}" + ' - veterinaria'

  
