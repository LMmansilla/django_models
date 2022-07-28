from django.contrib import admin
from django.urls import path

from proyect1.views import saludo, desafio, template_con_lista

urlpatterns = [
    path('admin/', admin.site.urls),
    path("saludo/", saludo, name="view_de_saludo"), 
    path("desafio/", desafio, name="desafio" ),
    path("template_con_lista/", template_con_lista, name= "template_con_lista")
]
