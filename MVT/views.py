from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template import loader

def padre (request):
    return render (request, "padre.html")

def index (request):
    return render (request, "index.html")

def inicio (request):
    return render(request, "inicio.html")

def en_construccion (request):
    return render (request, "en_construccion.html")