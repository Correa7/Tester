from django.db import models

class Refugio(models.Model):

    nombre = models.CharField(max_length= 80, unique=True)
    telefono = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    domicilio = models.TextField(max_length=200) 
    logo = models.ImageField(upload_to='refugio_image/', blank=True)
   



    def __str__(self):
        return f" {self.nombre} - {self.telefono} - {self.email} - {self.domicilio}"


class Perfil_Refugio (models.Model):

    refugio = models.OneToOneField('Refugio', on_delete=models.CASCADE, related_name='RefugioProf',null=True)

    description= models.TextField(max_length = 2000, null=True, blank=True)
    image_1 = models.ImageField(upload_to='refugio_image/', null=True, blank=True)
    image_2 = models.ImageField(upload_to='refugio_image/', null=True, blank=True)
    image_3 = models.ImageField(upload_to='refugio_image/', null=True, blank=True)
    image_4 = models.ImageField(upload_to='refugio_image/', null=True, blank=True)

    def __str__(self) -> str:
        return f" {self.description}"

    


