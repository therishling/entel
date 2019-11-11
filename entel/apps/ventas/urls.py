from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from apps.ventas import views as vista
urlpatterns = [
    path('dashboard/', login_required(vista.index) ,name='dashboard'),
    path('dashboard/admin/crearusuario', login_required(vista.CrearUsuario.as_view()) ,name='crear usuario'),
    path('dashboard/admin/listarusuario', login_required(vista.ListarUsuarios.as_view()) ,name='listar usuario'),
    re_path(r'^dashboard/admin/modificarusuario/(?P<pk>\d+)/$', login_required(vista.ModificarUsuarioAdmin.as_view()) ,name='modificar usuario'),
    re_path(r'^dashboard/admin/eliminarusuario/(?P<pk>\d+)/$', login_required(vista.EliminarUsuario.as_view()) ,name='eliminar usuario'),
]
