from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from blog.models import Viajes
from blog.forms import BlogForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):

    return render (request, "plantilla.html")



@login_required
def blogs(request):

    if request.method == "POST":

        blogs = BlogForm(request.POST, files=request.FILES)

        if blogs.is_valid():
            datos = blogs.cleaned_data

            contenidoBlog = Viajes(titulo=datos['titulo'] , subtitulo=datos['subtitulo'] ,contenido=datos['contenido'] , autor=datos['autor'] , creado=datos['creado'], imagen=request.FILES['imagen'])
            contenidoBlog.save()

            return render(request, "datosBlog.html")

    return render(request, "blogs.html")



def datosBlog(request):

    datos = Viajes.objects.all()
    dicc = {"datos":datos}
    plantillas = loader.get_template("datosBlog.html")
    documento = plantillas.render(dicc)
    return HttpResponse(documento)

@login_required
def eliminaBlog(request,id):
    
    datos = Viajes.objects.get(id=id)
    datos.delete()

    datos = Viajes.objects.all()

    return render(request,"datosBlog.html", {"datos":datos})


@login_required
def editarB(request,id):

    viaje = Viajes.objects.get(id=id)

    if request.method =="POST":
        form = BlogForm(request.POST, files=request.FILES)

        if form.is_valid():
            info = form.cleaned_data

            viaje.titulo=info['titulo']
            viaje.subtitulo=info['subtitulo']
            viaje.contenido=info['contenido']
            viaje.autor=info['autor']
            viaje.creado=info['creado']
            viaje.imagen=request.FILES['imagen']
            viaje.save()

            viaje = Viajes.objects.all()

            return render(request, "datosBlog.html", {"viajes":viaje})

    else:
        form = BlogForm(initial={'titulo':viaje.titulo, 'subtitulo':viaje.subtitulo, 'contenido':viaje.contenido, 'autor':viaje.autor, 'creado':viaje.creado, 'imagen':viaje.imagen,})

    return render(request, "editarBlog.html", {"form":form, "viajes":viaje})

