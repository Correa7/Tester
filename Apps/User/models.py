from django.db import models


class User_profile(models.Model):
    
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    first_name= models.CharField(max_length = 50, null=True, blank=True)
    last_name= models.CharField(max_length = 50, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    direccion= models.CharField(max_length=100, null=True, blank=True)
    description= models.TextField(max_length = 200, null=True, blank=True)
    image = models.ImageField(upload_to='profile_image/', null=True, blank=True)

    def __str__(self):
        return self.user.username + ' - profile'


        
