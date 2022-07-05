from time import time
from django.db import models
from datetime import datetime

# Create your models here.

class Turismo(models.Model):

    pais = models.CharField(max_length=80)
    ciudad = models.CharField(max_length=80)
    aventura = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=2000)
    operador = models.CharField(max_length=80)
    imagen = models.ImageField(upload_to="Turismo", null=True,blank=True)
    salida = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return self.pais