from django.http import HttpResponse
from datetime import datetime


from django.shortcuts import render


def saludo(request):
    return HttpResponse("Hola Mundo!!")

def canelones(request):
    return HttpResponse("Canelones de carne")

def dia_de_hoy(request):
    hoy = datetime.today().date()
    return HttpResponse(f"hoy es {hoy}")

def saludonombre(request, nombre):
    return HttpResponse(f"Hola amigo {nombre}")


def anionacimiento(request, edad):
    anioactual = datetime.today().year
    nacimiento = anioactual - edad
    return HttpResponse(f"Naciste en el {nacimiento}")

def plantilla(request):
    return render(request, "plantilla.html", context= {})


    