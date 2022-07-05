from django import forms
from datetime import datetime



class BlogForm(forms.Form):

    titulo = forms.CharField(max_length=80)
    subtitulo = forms.CharField(max_length=80)
    contenido = forms.CharField(max_length=2000)
    autor = forms.CharField(max_length=50)
    creado = forms.DateField()
    
