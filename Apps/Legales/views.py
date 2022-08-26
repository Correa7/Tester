from django.shortcuts import render
from django.http import HttpResponse

def preg_frecuentes (request):
    return render (request, "Legales/faqs.html")


def terminos (request):
    return render (request, "Legales/terminos.html")


def privacidad(request):
    return render (request,"Legales/privacidad.html")