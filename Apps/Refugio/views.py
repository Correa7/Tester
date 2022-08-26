from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
import datetime
from django.contrib.auth.decorators import login_required
from django.template import loader
from .models import Refugio,  Perfil_Refugio
from .forms import Refugio_form, Perfil_Refugio_Form
from django.views.generic import ListView, DetailView, CreateView, DeleteView

def Ficha_refugio (request):
    if request.method == "POST":
        miFormulario = Refugio_form(request.POST,request.FILES)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            ficha = Refugio(nombre = data["nombre"], telefono = data["telefono"], email= data["email"], domicilio= data["domicilio"], logo= data["logo"])
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


def lista_refugio (request):
    refugios = Refugio.objects.all() #Trae todos
    return render(request, 'Refugio/lista_refugio.html',{'refugios':refugios})      


class Detail_Refugio(DetailView):
    model = Refugio
    template_name = 'Refugio/detalle_refugio.html'

###################################################################


@login_required
def create_perfil_refugio(request):
    if request.method == "POST":
        form = Perfil_Refugio_Form(request.POST, request.FILES)
        if form.is_valid():
            Perfil_Refugio.objects.create (
                    descripcion= form.cleaned_data['descripcion'],
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


@login_required
def edit_perfil_refugio(request,id):
    if request.method == 'POST':
        form = Perfil_Refugio_Form(request.POST,request.FILES)
        if form.is_valid():
            perfil_refugio = Perfil_Refugio.objects.get(id=id)
            perfil_refugio.descripcion = form.cleaned_data['descripcion']
            perfil_refugio.image_1 = form.cleaned_data['image_1']
            perfil_refugio.image_2 = form.cleaned_data['image_2']
            perfil_refugio.image_3 = form.cleaned_data['image_3']
            perfil_refugio.image_4 = form.cleaned_data['image_4']
            perfil_refugio.save()
            return redirect('perfil-refugio')
    else:
        perfil_refugio = Perfil_Refugio.objects.get(id=id)
        form = Perfil_Refugio_Form(initial={
                                            "descripcion": perfil_refugio.descripcion,
                                            "image_1":  perfil_refugio.image_1,
                                            "image_2":  perfil_refugio.image_2,
                                            "image_3":  perfil_refugio.image_3,
                                            "image_4":  perfil_refugio.image_4,} )
        context = {'form':form}
        return render (request,'Refugio/edit_perfil_refugio.html',context)


@login_required
def eliminar_perfil_refugio(request,id):
    if request.method == 'GET':
        mensaje = 'Esta por borrar el perfil'
        perfil_refugio = Perfil_Refugio.objects.get(id=id)
        form = Perfil_Refugio_Form(initial={
                                            "descripcion": perfil_refugio.descripcion,
                                            "image_1":  perfil_refugio.image_1,
                                            "image_2":  perfil_refugio.image_2,
                                            "image_3":  perfil_refugio.image_3,
                                            "image_4":  perfil_refugio.image_4,} )    
        return render (request,'Refugio/del_perfil_refugio.html',{'form':form,'mensaje':mensaje})
    else:
        form = Perfil_Refugio.objects.get(id=id)
        form.delete()
        return redirect('index')




        

