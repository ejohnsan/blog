from django import forms
from datetime import datetime



class TurismoForm(forms.Form):

    pais = forms.CharField(max_length=80)
    ciudad = forms.CharField(max_length=80)
    aventura = forms.CharField(max_length=80)
    descripcion = forms.CharField(max_length=2000)
    operador = forms.CharField(max_length=80)
    salidad = forms.DateField()
    hora = forms.TimeField()
