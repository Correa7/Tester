from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.template import loader
from Apps.Veterinaria.models import Ficha_medica
from Apps.Veterinaria.forms import Ficha_form
from django.views.generic import  DeleteView
from django.views.generic.edit import UpdateView
from Apps.Mascota.models import Mascota



def Ficha_veterinaria (request, pk):  

    mascota= Mascota.objects.get(id=pk)
    print(mascota)
    print( "---------------debugueando-------------")

    if request.method == "POST":

        form = Ficha_form(request.POST)

        if form.is_valid():

            # data = form.cleaned_data

            # ficha = Ficha_medica(
                                
            #                     registro=data["registro"],
            #                     vacuna_1=data["vacuna_1"],
            #                     vacuna_2=data["vacuna_2"],
            #                     desparasitacion=data["desparasitacion"],
            #                     castracion=data["castracion"],
            #                     observaciones=["observaciones"],
            #                  )

            Ficha_medica.objects.create( 

                mascota= Mascota.objects.get(id=pk),
                registro = form.cleaned_data['registro'],
                vacuna_1 = form.cleaned_data['vacuna_1'],
                vacuna_2 = form.cleaned_data['vacuna_2'],
                desparasitacion = form.cleaned_data['desparasitacion'],
                castracion = form.cleaned_data['castracion'],
                observaciones = form.cleaned_data['observaciones'],
               
            )


            return redirect ( "lista-mascota")
    else:

        form = Ficha_form()    
    return render(request, "Veterinaria/ficha_veterinaria.html", {"form" : form})


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


def lista_fichas (request):
    lista = Ficha_medica.objects.all()
    return render (request, "Veterinaria/lista_Ficha.html", {"lista": lista})


class Borrar_Vacuna(DeleteView):

    model = Ficha_medica
    template_name= 'Veterinaria/borrar_vacuna.html'
    success_url = '/Mascota/lista-mascota/'


class Editar_Vacuna(UpdateView):

    model = Ficha_medica
    template_name = 'Veterinaria/editar_vacuna.html'
    fields = ["vacuna_1","vacuna_2","desparasitacion","castracion","observaciones"]
    success_url = '/Mascota/lista-mascota/'

