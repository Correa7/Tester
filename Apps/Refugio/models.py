from django.db import models

class Refugio(models.Model):

    nombre = models.CharField(max_length= 80, unique=True)
    telefono = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    domicilio = models.TextField(max_length=200) 
   


    def __str__(self):
        return f" {self.nombre} - {self.telefono} - {self.email} - {self.domicilio}"
