from django.db import models

# Create your models here.

class User_profile(models.Model):
    
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    
    first_name= models.CharField(max_length = 50, blank=True)
    last_name= models.CharField(max_length = 50, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    direccion= models.CharField(max_length=100, blank=True)
    description= models.TextField(max_length = 200, blank=True)
    image = models.ImageField(upload_to='profile_image/', blank=True)

    def __str__(self):
        return self.user.username + ' - profile'


        
