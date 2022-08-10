from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.template import loader
from Apps.Refugio.models import Refugio
from Apps.Refugio.forms import Refugio_form




def Ficha_refugio (request):

    if request.method == "POST":

        miFormulario = Refugio_form(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            ficha = Refugio(nombre = data["nombre"], telefono = data["telefono"], email= data["email"], domicilio= data["domicilio"])
            ficha.save()

            return render (request, "inicio.html" , context ={})
    else:

        miFormulario = Refugio_form() 

    return render(request, "Refugio/ficha_refugio.html", {"miFormulario" : miFormulario})




def busqueda_refugio (request):

    return render (request, "Refugio/ficha_busqueda_refugio.html")




def buscar_refugio (request):

    if request.GET["nombre"]:

        nombre= request.GET["nombre"]
        fichas= Refugio.objects.filter(nombre__icontains = nombre)
        return render(request, "Refugio/ficha_resultado_refugio.html", {"fichas": fichas,"nombre": nombre})

    else:
        respuesta ="No enviaste datos"

    return render (request, "inicio.html", {"respuesta": respuesta})

