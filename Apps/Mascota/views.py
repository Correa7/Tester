from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.template import loader
from Apps.Mascota.models import Mascota
from Apps.Mascota.forms import Mascota_form


def ficha_mascota (request):

    if request.method == "POST":

        form_mascotas = Mascota_form(request.POST, request.FILES)

        if form_mascotas.is_valid():

            # Mascota.objects.create(

            #         user = request.user,
            #         nickname = form_mascotas.cleaned_data['nickname'],
            #         especie = form_mascotas.cleaned_data['especie'],
            #         raza = form_mascotas.cleaned_data['raza'],
            #         sexo = form_mascotas.cleaned_data['sexo'],
            #         edad_aprox = form_mascotas.cleaned_data['edad_aprox'],
            #         ingreso = form_mascotas.cleaned_data['ingreso'],
            #         observaciones= form_mascotas.cleaned_data['observaciones'],
            #         image = form_mascotas.cleaned_data['image']
            #     )

            data = form_mascotas.cleaned_data

            ficha = Mascota(nickname = data['nickname'], especie = data['especie'],raza = data['raza'], sexo = data['sexo'],edad_aprox = data['edad_aprox'],ingreso = data['ingreso'], observaciones = data['observaciones'], image= data["image"],)
            
            ficha = ficha.save()
           
        return redirect ("lista-mascota")

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



def lista_mascota (request):

    mascotas = Mascota.objects.all() #Trae todos

    return render(request, 'Mascota/lista_mascota.html',{'mascotas':mascotas})      


   