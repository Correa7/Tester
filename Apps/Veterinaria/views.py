from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.template import loader
from Apps.Veterinaria.models import Ficha_medica
from Apps.Veterinaria.forms import Ficha_form

# Create your views here.


def Ficha_veterinaria (request):

    if request.method == "POST":

        miFormulario = Ficha_form(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            ficha = Ficha_medica(registro = data["registro"], vacuna_1 = data["vacuna_1"], vacuna_2 = data["vacuna_2"], desparasitacion= data["desparasitacion"], castracion= data["castracion"], observaciones= data["observaciones"])

            ficha.save()

            return render (request, "inicio.html" , context ={})

    else:

        miFormulario = Ficha_form()    

    return render(request, "Veterinaria/ficha_veterinaria.html", {"miFormulario" : miFormulario})



def busqueda_Vacuna (request):

    return render (request, "Veterinaria/ficha_busqueda_veterinaria.html")


def buscar_ficha (request):

    if request.GET["registro"]:

        registro= request.GET["registro"]
        fichas= Ficha_medica.objects.filter(registro__icontains = registro)

        return render(request, "Veterinaria/ficha_resultado_veterinaria.html", {"fichas": fichas,"registro": registro})

    else:

        respuesta ="No enviaste datos"

    return render (request, "inicio.html", {"respuesta": respuesta})