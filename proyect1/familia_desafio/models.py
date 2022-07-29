from django.db import models

class familia_desafio(models.Model):
    nombre = models.CharField(max_length= 50)
    apellido = models.CharField(max_length= 50)
    dni = models.IntegerField(default="unknow")
    habita_en_casa = models.BooleanField(default=True)
    edad = models.DateField(auto_now_add=True, blank=True, null=True)

