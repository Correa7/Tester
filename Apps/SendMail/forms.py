from tkinter.tix import Form
from django import forms

class adopcionForm (forms.Form):
    nombre = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Ingresa tu nombre'}) )
    email = forms.EmailField(label='Email  ',widget=forms.TextInput(attrs={'placeholder':'Ingresa tu email'}),required=True)
    mascota = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Nombre de la Mascota'}) )


class VoluntarioForm (forms.Form):
    nombre = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Ingresa tu nombre'}) )
    email = forms.EmailField(label='Email  ',widget=forms.TextInput(attrs={'placeholder':'Ingresa tu email'}),required=True)
    refugio = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Nombre del Refugio'}) )


class donacionForm (forms.Form):
    nombre = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Ingresa tu nombre'}) )
    email = forms.EmailField(label='Email  ',widget=forms.TextInput(attrs={'placeholder':'Ingresa tu email'}),required=True)


class newsForm (forms.Form):
    nombre = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Ingresa tu nombre'}) )
    email = forms.EmailField(label='Email  ',widget=forms.TextInput(attrs={'placeholder':'Ingresa tu email'}),required=True)
