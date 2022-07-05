from django.shortcuts import render
from django.http import HttpResponse
from tour.models import Turismo
from tour.forms import TurismoForm
from django.template import loader
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def tour(request):

    if request.method == "POST":

        tour = TurismoForm(request.POST, files=request.FILES)

        if tour.is_valid():
            data = tour.cleaned_data

            contenido = Turismo(pais=data['pais'] , ciudad=data['ciudad'] , aventura=data['aventura'] , descripcion=data['descripcion'] , operador=data['operador'] , imagen=request.FILES['imagen'] , salida=data['salida'] , hora=data['hora'])
            contenido.save()

            return render(request, "datosTour.html")
    
    return render(request, "tour.html")




def datosTour(request):

    datos = Turismo.objects.all()
    dicc = {"datos":datos}
    plantillas = loader.get_template("datosTour.html")
    documento = plantillas.render(dicc)
    return HttpResponse(documento)


@login_required
def eliminaTour(request,id):
    
    datos = Turismo.objects.get(id=id)
    datos.delete()

    datos = Turismo.objects.all()

    return render(request,"datosTour.html", {"datos":datos})


@login_required
def editarT(request,id):

    tour = Turismo.objects.get(id=id)

    if request.method =="POST":
        form = TurismoForm(request.POST, files=request.FILES)

        if form.is_valid():
            info = form.cleaned_data

            tour.pais=info['pais']
            tour.ciudad=info['ciudad']
            tour.aventura=info['aventura']
            tour.descripcion=info['descripcion']
            tour.operador=info['operador']
            tour.imagen=request.FILES['imagen']
            tour.salida=info['salida']
            tour.hora=info['hora']
            tour.save()

            tour = Turismo.objects.all()

            return render(request, "datosTour.html", {"tour":tour})

    else:
        form = TurismoForm(initial={'pais':tour.pais, 'ciudad':tour.ciudad, 'aventura':tour.aventura, 'descripcion':tour.descripcion, 'operador':tour.operador, 'imagen':tour.imagen, 'salida':tour.salida, 'hora':tour.hora})

    return render(request, "editarTour.html", {"form":form, "tour":tour})


