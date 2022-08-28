from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.template import loader
from Apps.Mascota.models import Mascota
from Apps.Mascota.forms import Mascota_form
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.views.generic.edit import UpdateView

def ficha_mascota (request):

    if request.method == "POST":

        form = Mascota_form(request.POST, request.FILES)

        if form.is_valid():
      
            data = form.cleaned_data
            ficha = Mascota(nickname = data['nickname'], especie = data['especie'],raza = data['raza'], sexo = data['sexo'],edad_aprox = data['edad_aprox'],ingreso = data['ingreso'], observaciones = data['observaciones'], image= data["image"],)
           
            ficha = ficha.save()

        return redirect ("lista-mascota")
    else:
        
        form = Mascota_form()

    return render(request,'Mascota/ficha_mascotas.html',{"form" : form})


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


class Detail_Mascota(DetailView):
    model = Mascota
    template_name = 'Mascota/detalle_mascota.html'



class Borrar_Mascota(DeleteView):

    model = Mascota
    template_name= 'Mascota/borrar_mascota.html'
    success_url = '/Mascota/lista-mascota/'


class Editar_Mascota(UpdateView):

    model = Mascota
    template_name = 'Mascota/editar_mascota.html'
    fields = ["nickname","especie","raza","sexo","edad_aprox","ingreso","observaciones", "image"]
    success_url = '/Mascota/lista-mascota/'

  