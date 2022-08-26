
from tkinter.tix import Form
from django import forms

class newsForm (forms.Form):
    nombre = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Ingresa tu nombre'}) )
    email = forms.EmailField(label='Email  ',widget=forms.TextInput(attrs={'placeholder':'Ingresa tu email'}),required=True)
