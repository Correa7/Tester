from django.db import models

class Mascota (models.Model):
    nickname = models.CharField(max_length= 50, unique=True)
    especie = models.CharField(max_length= 50)
    raza = models.CharField(max_length= 50)
    sexo = models.CharField (max_length= 20)
    edad_aprox= models.IntegerField()
    ingreso = models.DateField()
    observaciones = models.TextField(max_length=80,null=True, blank=True)

    def __str__(self):
         return f" {self.nickname} - {self.especie} - {self.raza} - {self.sexo} - {self.edad_aprox} - {self.ingreso}"