from django.urls import path
from . import views



urlpatterns = [
    
    path("tour", views.tour, name="tour"),
    path("datosTour", views.datosTour, name="datosTour"),
    path("eliminaTour", views.eliminaTour, name="eliminaTour"),
    path("editarT", views.editarT, name="editarT")
]
