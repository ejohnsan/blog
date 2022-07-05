from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserEditForm




# Create your views here.


def loginT(request):

    if request.method == "POST":

        form = AuthenticationForm(request , data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password=contra)

            if user is not None:
                login(request,user)
                return render(request, "plantilla.html", {"mensaje":f"Bienvenido{usuario}"})

            else:
                return HttpResponse("Ususario incorrecto")
        else:
            return HttpResponse(f"FORMULARIO INCORRECTO {form}")
    form = AuthenticationForm()

    return render(request, 'loginTour.html', {"form":form})




def register(request):

    if request.method == "POST":
        
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()

            return render(request, "plantilla.html", {"mensaje":"Usuario creado"})

    else:
        form = UserRegisterForm()

    return render(request, "registro.html", {"form":form})



@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == "POST":
        form = UserEditForm(request.POST)

        if form.is_valid():
            info = form.cleaned_data

            usuario.email = info['email']
            password = info['password1']
            usuario.set_password('password')
            usuario.save()

            return render(request, "plantilla.html")

    else:
        form = UserEditForm(initial={'email':usuario.email})
    
    return render(request, "editarPerfil.html", {"form":form, "usuario":usuario})





def about(request):

    return render(request, "about.html")
