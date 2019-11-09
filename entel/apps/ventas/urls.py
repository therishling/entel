from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from apps.ventas import views as vista
urlpatterns = [
    path('dashboard/', login_required(vista.index) ,name='dashboard'),
    path('dashboard/crearusuario', login_required(vista.CrearUsuario.as_view()) ,name='crear usuario'),
]
