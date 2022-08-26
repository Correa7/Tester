from django.http import HttpResponse
import datetime
from django.template import loader
from django.shortcuts import render, redirect
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.decorators import login_required
from .forms import  newsForm 

def padre (request):
    return render (request, "padre.html")


def index (request):
    return render (request, "index.html")


def inicio (request):
    return render(request, "inicio.html")


def en_construccion (request):
    return render (request, "en_construccion.html")


def sobre_nosotros (request):
    return render (request, "sobre_nosotros.html")


def presentacion (request):
    return render (request, "presentacion.html")


def voluntarios (request):
    return render (request, "voluntarios.html")


def requerimiento (request):
    return render (request, "requerimiento.html")


##############################################################


def send_index(mail):
    context= {"mail": mail}
    template = get_template("SendMail/correo_adopcion.html")
    content = template.render(context)
    email = EmailMultiAlternatives(
        "Newsletter",
        "Noticias Salvando Patitas",
        settings.EMAIL_HOST_USER,
        [mail],
    )

    email.attach_alternative(content,"Text/html")
    email.send()
    return redirect ("inicio")

# @login_required

def form_index(request):

    if request.method == "POST":

        form = newsForm(request.POST)
    
        if form.is_valid():

            nombre= form.cleaned_data["nombre"]
            email= form.cleaned_data["email"]
            print(email)

            mail = request.POST.get("email")

            print(mail)

            send_index(mail)
    
            respuesta= f"Felicidades has completado el primer paso para Adoptar una mascota, no olvides revisar tu casilla de correos para continuar con la postulacion"

        return render (request, "inicio.html", {"respuesta":respuesta})


    else:
     
        form= newsForm ()
     
    return render (request, "index.html", {"form":form})
    


########################################################################


