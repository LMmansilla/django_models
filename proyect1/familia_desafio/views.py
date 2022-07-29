from django.shortcuts import render
from familia_desafio.models import Familia_desafio


def creacion_integrantes(request):
    integ1= Familia_desafio.objects.create(nombre= "jorge", apellido = "perez", dni = 20555555, habita_en_casa = True, edad = 40)
    integ2= Familia_desafio.objects.create(nombre= "Lucia", apellido = "perez", dni = 45786658, habita_en_casa = False, edad = 55)
    integ3= Familia_desafio.objects.create(nombre= "David", apellido = "perez", dni = 13215455, habita_en_casa = True, edad = 20)
    integ4= Familia_desafio.objects.create(nombre= "Anto", apellido = "perez", dni = 78945561, habita_en_casa = False, edad = 15)
    context= {
        "integ1" : integ1,
        "integ2" : integ2,
        "integ3" : integ3,
        "integ4" : integ4
    }
    return render(request, "datos-familia.html", context=context)

def todos(request):
    todos_los_integrantes = Familia_desafio.objects.all()
    context = {
        "personas" : todos_los_integrantes
    }
    return render(request, "todos_los_integrantes.html", context= context)



