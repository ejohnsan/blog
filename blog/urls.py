from django.urls import path
from . import views



urlpatterns = [
    
    path("", views.home, name="home"),
    path("blogs", views.blogs, name="blogs"),
    path("datosBlog", views.datosBlog, name="datosBlog"),
    path("eliminaBlog/<int:id>", views.eliminaBlog, name="eliminaBlog"),
    path("editarB/<int:id>", views.editarB, name="editarB"),
    path("editarB", views.editarB, name="editarB"),
    
]

