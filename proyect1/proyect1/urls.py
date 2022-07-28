from django.contrib import admin
from django.urls import path


from proyect1.views import saludo, desafio



urlpatterns = [
    path('admin/', admin.site.urls),
    path("saludo/", saludo, name="view_de_saludo"), 
    path("desafio/", desafio, name="desafio" )
]
