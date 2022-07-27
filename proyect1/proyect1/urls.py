from django.contrib import admin
from django.urls import path


from proyect1.views import saludo, canelones, dia_de_hoy, saludonombre, anionacimiento, plantilla



urlpatterns = [
    path('admin/', admin.site.urls),
    path("saludo/", saludo, name="view_de_saludo"), 
    path("canelones/", canelones, name= "canelones"),
    path("dia-de-hoy/", dia_de_hoy, name = "dia de hoy"),
    path("saludo-con-nombre/<str:nombre>", saludonombre, name = "saludo con nombre"),
    path("nacimiento/<int:edad>", anionacimiento, name= "nacimiento"),
    path("plantilla/", plantilla, name="plantilla")
]
