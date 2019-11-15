from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from apps.ventas import views as vista
urlpatterns = [
    #INDEX
    path('dashboard/', login_required(vista.Index.as_view()) ,name='dashboard'),
    # CRUD USUARIO
    path('dashboard/admin/crearusuario', login_required(vista.CrearUsuario.as_view()) ,name='crear usuario'),
    path('dashboard/admin/listarusuario', login_required(vista.ListarUsuarios.as_view()) ,name='listar usuario'),
    re_path(r'^dashboard/admin/modificarusuario/(?P<pk>\d+)/$', login_required(vista.ModificarUsuarioAdmin.as_view()) ,name='modificar usuario'),
    re_path(r'^dashboard/admin/eliminarusuario/(?P<pk>\d+)/$', login_required(vista.EliminarUsuario.as_view()) ,name='eliminar usuario'),
    # ACTUALIZAR PERFIL
    re_path(r'^dashboard/modificarperfil/(?P<pk>\d+)/$', login_required(vista.ModificarPerfil.as_view()) ,name='modificar perfil'),
    # CRUD PRODUCTO
    path('dashboard/admin/crearproducto', login_required(vista.CrearProducto.as_view()) ,name='crear producto'),
    path('dashboard/admin/listarproducto', login_required(vista.ListarProductos.as_view()) ,name='listar producto'),
    re_path(r'^dashboard/admin/modificarproducto/(?P<pk>\d+)/$', login_required(vista.ModificarProducto.as_view()) ,name='modificar producto'),
    re_path(r'^dashboard/admin/eliminarproducto/(?P<pk>\d+)/$', login_required(vista.EliminarProducto.as_view()) ,name='eliminar producto'),

    #VENTAS
    path('dashboard/vendedor/venta', login_required(vista.CrearVenta.as_view()) ,name='crear venta'),
    path('dashboard/vendedor/listaventas', login_required(vista.ListarVenta.as_view()) ,name='listar venta'),
]
