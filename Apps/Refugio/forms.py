from contextlib import nullcontext
from django import forms
from django.forms import ModelForm
from .models import Perfil_Refugio, Refugio

class Refugio_form (forms.Form):
    
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Ingrese el Nombre'}))
    telefono = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Ingrese número entero'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Ingrese E-mail'}))
    domicilio = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Ingrese la Direccion'}))
    logo = forms.ImageField(label='Imagen  ')

    class Meta:
        model = Refugio
        fields = ['nombre','telefono','email','domicilio','logo']
        help_texts = {k:'' for k in fields}
##############################################################

        
class Perfil_Refugio_Form(forms.Form):
    description = forms.CharField(max_length= 2000,widget=forms.TextInput(attrs={'placeholder':'Ingrese texto'}),required=False)
    image_1 = forms.ImageField(required=False)
    image_2 = forms.ImageField(required=False)
    image_3 = forms.ImageField(required=False)
    image_4 = forms.ImageField(required=False)

    class Meta:
        model = Perfil_Refugio
        fields = ['description','image_1','image_2','image_3','image_4']
        help_texts = {k:'' for k in fields}