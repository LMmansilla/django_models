from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def saludo(request):
    return HttpResponse("Hola Mundo!!")

def desafio(request):
    today = datetime.now()
    context = {
        'nombre' : 'juan',
        'apellido' : 'Perez',
        'today' : today
    }
    return render(request, "desafio.html", context = context)

def template_con_lista(request):
    context = {
        "lista" : ["tomate", "naranja", "banana"]
    }
    return render(request, "template_con_lista.html", context = context)