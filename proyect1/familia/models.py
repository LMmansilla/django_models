from django.db import models

class familia(models.Model):
    nombre = models.CharField(max_length= 50)
    apellido = models.CharField(max_length= 50)
    habita_en_casa = models.BooleanField(default=True)
    edad = models.DateField(auto_now_add=True, blank=True, null=True)
