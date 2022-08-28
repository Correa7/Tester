from contextlib import nullcontext
from logging import PlaceHolder
from django import forms
from django.forms import ModelForm
from .models import Mascota

#Variables para los ChoiceField
sexos = [(' Macho',' Macho'),(' Hembra',' Hembra')]
lista_especies = [(' Perro',' Perro'),(' Gato',' Gato')]


class Mascota_form (forms.Form):
    nickname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Ingrese texto'}))
    especie = forms.ChoiceField(choices=lista_especies,required=True,label='Seleccione la especie')
    raza = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Ingrese texto'}))
    sexo =  forms.ChoiceField(choices=sexos,required=True,label='Seleccione el sexo')
    edad_aprox= forms.IntegerField(label='Edad aproximada',widget=forms.TextInput(attrs={'placeholder':'Ingrese número entero'}))
    ingreso = forms.DateField(widget=forms.TextInput(attrs={'placeholder':'Formato AAAA-MM-DD'}))
    observaciones = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Ingrese texto'}))
    image = forms.ImageField(label='Imagen  ')

    class Meta:
        model = Mascota
        # fields = (
            # 'nickname',
            # 'especie',
            # 'raza',
            # 'sexo',
            # "edad_aprox",
            # "ingreso",
            # "observaciones",
            # "image",
            #    )