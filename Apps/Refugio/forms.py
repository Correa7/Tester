from contextlib import nullcontext
from django import forms

class Refugio_form (forms.Form):

    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Ingrese el Nombre'}))
    telefono = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Ingrese número entero'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Ingrese E-mail'}))
    domicilio = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Ingrese la Direccion'}))
