from django.db import models
from datetime import datetime


# Create your models here.


class Viajes(models.Model):
    
    titulo = models.CharField(max_length=80)
    subtitulo = models.CharField(max_length=80)
    contenido = models.CharField(max_length=2000)
    autor = models.CharField(max_length=50)
    creado = models.DateField()
    imagen = models.ImageField(upload_to='blogViajes',null=True,blank=True)

    def __str__(self):
        return self.titulo

