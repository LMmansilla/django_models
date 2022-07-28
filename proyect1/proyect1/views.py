from django.http import HttpResponse

from django.shortcuts import render


def saludo(request):
    return HttpResponse("Hola Mundo!!")

def desafio(request):
    return render(request, "desafio.html", context={})

