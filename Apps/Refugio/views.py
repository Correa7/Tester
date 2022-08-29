from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
import datetime
from django.contrib.auth.decorators import login_required
from django.template import loader
from .models import Refugio,  Perfil_Refugio
from .forms import Refugio_form, Perfil_Refugio_Form
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.views.generic.edit import UpdateView




def Ficha_refugio (request):

    if request.method == "POST":

        form = Refugio_form(request.POST, request.FILES)

        if form.is_valid():

            # data = form.cleaned_data
            # ficha = Refugio(nombre = data["nombre"], telefono = data["telefono"], email= data["email"], domicilio= data["domicilio"], logo= data["logo"],)
            # ficha = ficha.save()

            Refugio.objects.create (

                nombre= form.cleaned_data['nombre'],
                telefono = form.cleaned_data['telefono'],
                email = form.cleaned_data['email'],
                domicilio = form.cleaned_data['domicilio'],
                logo = form.cleaned_data['logo'],
                )

            return redirect ( "lista-refugio")

    else:

        form = Refugio_form() 
    return render(request, "Refugio/ficha_refugio.html", {"form" : form})



def buscar_refugio (request):

    if request.GET["nombre"]:
        nombre= request.GET["nombre"]
        fichas= Refugio.objects.filter(nombre__icontains = nombre)
        return render(request, "Refugio/ficha_resultado_refugio.html", {"fichas": fichas,"nombre": nombre})
    else:
        respuesta ="No enviaste datos"
    return render (request, "inicio.html", {"respuesta": respuesta})


def lista_refugio (request):
    refugios = Refugio.objects.all() #Trae todos
    return render(request, 'Refugio/lista_refugio.html',{'refugios':refugios})      


class Detail_Refugio(DetailView):
    model = Refugio
    template_name = 'Refugio/detalle_refugio.html'


class Borrar_Refugio(DeleteView):

    model = Refugio
    template_name= 'Refugio/borrar_refugio.html'
    success_url = '/Refugio/lista-refugio/'


class Editar_Refugio(UpdateView):

    model = Refugio
    template_name = 'Refugio/editar_refugio.html'
    fields = ["nombre","telefono","email","domicilio","logo"]
    success_url = '/Refugio/lista-refugio/'




###################################################################


@login_required
def create_perfil_refugio(request, id):
    
    refugio= Refugio.objects.get(id=id)

    if request.method == "POST":
        form = Perfil_Refugio_Form(request.POST, request.FILES)
        if form.is_valid():

            Perfil_Refugio.objects.create (

                    refugio= Refugio.objects.get(id=id),
                    description= form.cleaned_data['description'],
                    image_1 = form.cleaned_data['image_1'],
                    image_2 = form.cleaned_data['image_2'],
                    image_3 = form.cleaned_data['image_3'],
                    image_4 = form.cleaned_data['image_4'],
                )

            return redirect ("lista-refugio")
        else:
            return render (request, "Refugio/respuesta_refugio.html", {"context":f"los cambios no se han realizado"})
    else:

        form = Perfil_Refugio_Form()

        return render (request, "Refugio/crear_perfil_refugio.html",{"form":form})


def show_perfil_refugio (request):
    refugio = Perfil_Refugio.objects.all()
    return render(request, 'Refugio/perfil_refugio.html', {"refugio":refugio})

        
class Borrar_Refugio_Perfil(DeleteView):

    model = Perfil_Refugio
    template_name= 'Refugio/del_perfil_refugio.html'
    success_url = '/Refugio/lista-refugio/'


class Editar_Refugio_Perfil(UpdateView):

    model = Perfil_Refugio
    template_name = 'Refugio/edit_perfil_refugio.html'
    fields = ["description","image_1","image_2","image_3","image_4"]
    success_url = '/Refugio/lista-refugio/'

