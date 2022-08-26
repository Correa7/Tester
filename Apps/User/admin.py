from email.mime import image
from django.contrib import admin
from Apps.User.models import User_profile

@admin.register(User_profile)
class User_profile_admin(admin.ModelAdmin):
    list_display = ['user','first_name','last_name', 'phone', 'direccion', 'description','image']

