from django.db import models

class Mascota (models.Model):
    nickname = models.CharField(max_length= 50, unique=True)
    especie = models.CharField(max_length= 50, null=True, blank=True)
    raza = models.CharField(max_length= 50, null=True, blank=True)
    sexo = models.CharField (max_length= 20, null=True, blank=True)
    edad_aprox= models.IntegerField(null=True, blank=True)
    ingreso = models.DateField(null=True, blank=True)
    observaciones = models.TextField(max_length=80,null=True, blank=True)
    image = models.ImageField(upload_to='mascota_image/', null=True, blank=True)


    def __str__(self):
         return f" {self.nickname} - {self.especie} - {self.raza} - {self.sexo} - {self.edad_aprox} - {self.ingreso}"