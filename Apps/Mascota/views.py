from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.template import loader
from Apps.Mascota.models import Mascota
from Apps.Mascota.forms import Mascota_form

def ficha_mascota (request):
    if request.method == "POST":
        form_mascotas = Mascota_form(request.POST)
        if form_mascotas.is_valid():
            data = form_mascotas.cleaned_data
            ficha = Mascota(nickname = data['nickname'], especie = data['especie'],raza = data['raza'], sexo = data['sexo'],edad_aprox = data['edad_aprox'],ingreso = data['ingreso'], observaciones = data['observaciones'],)
            ficha = ficha.save()
            # return redirect(inicio)
            return render (request, "inicio.html" , context ={})
    else:
        form_mascotas = Mascota_form()

    return render(request,'Mascota/ficha_mascotas.html',{"form_mascotas": form_mascotas})

def busqueda_mascota (request):
    return render (request, "Mascota/ficha_busqueda_mascotas.html")

def buscar_mascota (request):
    if request.GET["nickname"]:
        nickname= request.GET["nickname"]
        fichas= Mascota.objects.filter(nickname__icontains = nickname)
        return render(request, "Mascota/ficha_resultado_mascotas.html", {"fichas":fichas,"nickname":nickname})
    else:
        respuesta ="No enviaste datos"
    return render (request, "inicio.html", {"respuesta": respuesta})
