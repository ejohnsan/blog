from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    
    path('loginT', views.loginT, name="loginT"),
    path("register", views.register, name="register"),
    path("logout", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("editarPerfil", views.editarPerfil, name="editarPerfil"),
    path("about", views.about, name="about"),

]
