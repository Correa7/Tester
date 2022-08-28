from django.shortcuts import render, redirect
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.decorators import login_required
from .forms import adopcionForm, VoluntarioForm, donacionForm, newsForm



def send_mascota(mail):
    context= {"mail": mail}
    template = get_template("SendMail/correo_adopcion.html")
    content = template.render(context)
    email = EmailMultiAlternatives(
        "Adopcion",
        "Adoptar nos hace fellices",
        settings.EMAIL_HOST_USER,
        [mail],
    )

    email.attach_alternative(content,"Text/html")
    email.send()
    return redirect ("inicio")

@login_required
def form_adopcion(request):
    if request.method == "POST":
        form = adopcionForm(request.POST)    
        if form.is_valid():
            nombre= form.cleaned_data["nombre"]
            email= form.cleaned_data["email"]
            print(email)
            mail = request.POST.get("email")
            print(mail)
            send_mascota(mail)    
            respuesta= f"Felicidades has completado el primer paso para Adoptar una mascota, no olvides revisar tu casilla de correos para continuar con la adopción"
        return render (request, "inicio.html", {"respuesta":respuesta})
    else:     
        form= adopcionForm()     
    return render (request, "SendMail/form_adopcion.html", {"form":form})
    
##################################################

def send_voluntario (mail):

    context= {"mail": mail}
    print(context)
    template = get_template("SendMail/correo_voluntario.html")
    content = template.render(context)
    email = EmailMultiAlternatives(
        "Formulario postulacion Voluntario",
        "Voluntario para salvar patitas",
        settings.EMAIL_HOST_USER,
        [mail],
    )

    email.attach_alternative(content,"Text/html")
    email.send()

    

@login_required
def form_voluntario (request):

    if request.method == "POST":
        form = VoluntarioForm(request.POST)   
        if form.is_valid():
            nombre= form.cleaned_data["nombre"]
            email= form.cleaned_data["email"]
            refugio= form.cleaned_data["refugio"]
            print(email)

            mail = request.POST.get("email")

            print(mail)

            send_voluntario(mail)

            respuesta= f"Ya casi eres un Voluntario!!, continua tu postulacion siguiendo las instrucciones del mail que te enviamos, no olvides revisar tu casilla de correos"

        return render (request, "inicio.html", {"respuesta":respuesta})
    else:
        form= VoluntarioForm()
    return render (request, "SendMail/form_voluntario.html", {"form":form})
     

###########################################################


def send_donar (mail):
    context= {"mail": mail}
    template = get_template("SendMail/correo_donacion.html")
    content = template.render(context)
    email = EmailMultiAlternatives(
        "Formulario postulacion Voluntario",
        "Voluntario para salvar patitas",
        settings.EMAIL_HOST_USER,
        [mail],
    )

    email.attach_alternative(content,"Text/html")
    email.send()


@login_required
def form_donar(request):

    if request.method == "POST":
        form = donacionForm(request.POST)
        if form.is_valid():
            nombre= form.cleaned_data["nombre"]
            email= form.cleaned_data["email"]
            print(email)
            mail = request.POST.get("email")
            print(mail)
            send_donar(mail)
    
            respuesta= f"Muchas gracias, tu donacion nos ayuda a seguir creciendo, no olvides revisar tu casilla de correos para continuar con la postulacion"

        return render (request, "inicio.html", {"respuesta":respuesta})
    else:
        form= donacionForm()
     
    return render (request, "SendMail/form_donar.html", {"form":form})
    
    
    
################################################################



def send_newsletter(mail):

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




def form_newsletter(request):
    if request.method == "POST":
        form = newsForm(request.POST)
        if form.is_valid():
            nombre= form.cleaned_data["nombre"]
            email= form.cleaned_data["email"]
            print(email)
            mail = request.POST.get("email")
            print(mail)

            send_newsletter(mail)
    
            respuesta= f"Gracias por contactar con nosotros, en breve te llegara un correo con todas las novedades de Salvando Patitas"

        return render (request, "inicio.html", {"respuesta":respuesta})
       

    else:
        form= newsForm ()
    return render (request, "SendMail/form_newsletter.html", {"form":form})
    

