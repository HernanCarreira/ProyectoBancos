from django.http import HttpResponse
from django.shortcuts import render
from Apptasasbancos.models import Bancos

from django.http import HttpResponse


# Create your views here.
def inicio (request):
    return render(request, "Apptasasbancos/inicio.html")

def bancos (request):
    return render (request, "Apptasasbancos/bancos.html")

def tasas (request):
    return render (request, "Apptasasbancos/tasas.html")

def productos (request):
    return render (request, "Apptasasbancos/productos.html")

def leerbancos(request):
    bancos = Bancos.objects.all()
    return render(request, "Apptasasbancos/leerbancos.html", {"bancos":bancos})
