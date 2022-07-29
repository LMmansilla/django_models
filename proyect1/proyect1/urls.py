from django.contrib import admin
from django.urls import path

from familia_desafio.views import creacion_integrantes, todos

urlpatterns = [
    path('admin/', admin.site.urls),
    path("creacion_integrantes/", creacion_integrantes, name="creacion_integrantes"),
    path("lista_integrantes/", todos, name="todos")   
]
