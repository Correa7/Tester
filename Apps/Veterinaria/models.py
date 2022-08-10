from django.db import models

# Create your models here.

class Ficha_medica (models.Model):

    registro = models.IntegerField(unique=True)
    vacuna_1 = models.CharField(max_length= 100, null=True, blank=True,)
    vacuna_2 = models.CharField(max_length= 100, null=True, blank=True,)
    desparasitacion = models.CharField(max_length=50, null=True, blank=True,)
    castracion = models.CharField(max_length=50, null=True, blank=True,)
    observaciones = models.TextField(max_length=150,null=True, blank=True,)


    def __str__(self) -> str:
        return f" {self.registro} - {self.vacuna_1} - {self.vacuna_2} - {self.desparacitacion} - {self.castracion} - {self.observaciones}"

  
