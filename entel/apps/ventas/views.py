from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView,CreateView,UpdateView,DeleteView, TemplateView
from django.urls import reverse,reverse_lazy
from apps.ventas import models as modelos
from apps.ventas import forms as formularios
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin



# Create your views here.
class Index(TemplateView):
    template_name = 'dashboard/index.html'

# Funcionalidades ADMIN

#USUARIOS

class CrearUsuario(UserPassesTestMixin, SuccessMessageMixin, CreateView):

    model = modelos.Vendedor
    form_class = formularios.CrearUsuario
    template_name = 'dashboard/admin/usuario/formvendedor.html'
    success_message = 'Usuario registrado correctamente'
    success_url = reverse_lazy('crear usuario')
    
    def test_func(self):
        user = self.request.user
        return user.admin
    
    def handle_no_permission(self):
        return redirect('dashboard')

class ListarUsuarios(UserPassesTestMixin, ListView):
    model = modelos.Vendedor
    template_name = 'dashboard/admin/usuario/listausuario.html'
    context_object_name = 'usuarios'

    def test_func(self):
        user = self.request.user
        return user.admin
    
    def handle_no_permission(self):
        return redirect('dashboard')
        

    
class ModificarUsuarioAdmin(UserPassesTestMixin, UpdateView):
    model = modelos.Vendedor
    form_class = formularios.ModificarUsuario
    template_name = 'dashboard/admin/usuario/formvendedor.html'
    success_url = reverse_lazy('listar usuario')
    context_object_name = 'usuario'
    def test_func(self):
        user = self.request.user
        return user.admin
    
    def handle_no_permission(self):
        return redirect('dashboard')

class EliminarUsuario(UserPassesTestMixin, DeleteView):
    model = modelos.Vendedor
    template_name = 'dashboard/admin/usuario/listausuario.html'
    success_url = reverse_lazy('listar usuario')
    context_object_name = 'usuario'
    def test_func(self):
        user = self.request.user
        return user.admin
    
    def handle_no_permission(self):
        return redirect('dashboard')

#PRODUCTOS

class CrearProducto(UserPassesTestMixin, SuccessMessageMixin, CreateView):
    model = modelos.Producto
    form_class = formularios.ProductoForm
    template_name = 'dashboard/admin/producto/formproducto.html'
    success_message = 'Producto Creado Correctamente'
    success_url = reverse_lazy('crear producto')
    
    def test_func(self):
        user = self.request.user
        return user.admin
    
    def handle_no_permission(self):
        return redirect('dashboard')

class ListarProductos(UserPassesTestMixin, ListView):
    model = modelos.Producto
    template_name = 'dashboard/admin/producto/listaproducto.html'
    context_object_name = 'productos'

    def test_func(self):
        user = self.request.user
        return user.admin
    
    def handle_no_permission(self):
        return redirect('dashboard')

class ModificarProducto(UserPassesTestMixin, UpdateView):
    model = modelos.Producto
    form_class = formularios.ProductoForm
    template_name = 'dashboard/admin/producto/formproducto.html'
    success_url = reverse_lazy('listar producto')
    context_object_name = 'producto'
    def test_func(self):
        user = self.request.user
        return user.admin
    
    def handle_no_permission(self):
        return redirect('dashboard')

class EliminarProducto(UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = modelos.Producto
    template_name = 'dashboard/admin/producto/listaproducto.html'
    success_message = 'Producto Eliminado'
    success_url = reverse_lazy('listar producto')
    context_object_name = 'producto'
    def test_func(self):
        user = self.request.user
        return user.admin
    
    def handle_no_permission(self):
        return redirect('dashboard')


# VISTA USUARIOS

class ModificarPerfil(UserPassesTestMixin,SuccessMessageMixin,UpdateView):
    model = modelos.Vendedor
    form_class = formularios.ModificarUsuario
    template_name = 'dashboard/admin/usuario/formvendedor.html'
    success_url = reverse_lazy('dashboard')
    context_object_name = 'usuario'
    success_message = 'Perfil Actualizado'
    def test_func(self):
        user = str(self.request.user.id)
        path = self.request.path
        path = path.replace("/dashboard/modificarperfil/","")
        path = path.replace("/","")
        if user == path:
            return True
        return False
    
    def handle_no_permission(self):
        return redirect('dashboard')

class ModificarPassword(UserPassesTestMixin,SuccessMessageMixin,UpdateView):
    model = modelos.Vendedor
    form_class = formularios.ModificarPassword
    template_name = 'dashboard/admin/usuario/formpassword.html'
    success_url = reverse_lazy('dashboard')
    context_object_name = 'usuario'
    success_message = 'Password Actualizado'
    def test_func(self):
        user = str(self.request.user.id)
        path = self.request.path
        path = path.replace("/dashboard/modificarpassword/","")
        path = path.replace("/","")
        if user == path:
            return True
        return False
    
    def handle_no_permission(self):
        return redirect('dashboard')



class CrearVenta(SuccessMessageMixin,UserPassesTestMixin,CreateView):
    model = modelos.Venta
    template_name = 'dashboard/vendedor/venta/formventas.html'
    success_url =  reverse_lazy('crear venta')
    form_class = formularios.VentaForms
    success_message = 'venta creada'
    context_object_name = 'venta'

    def test_func(self):
        user = self.request.user
        return user.is_vendedor
    
    def handle_no_permission(self):
        return redirect('dashboard')

class ListarVenta(ListView, UserPassesTestMixin):
    model = modelos.Venta
    template_name = 'dashboard/vendedor/venta/lista.html'
    context_object_name = 'ventas'

    def get_context_data(self, **kwargs):
        context = super(ListarVenta, self).get_context_data(**kwargs)
        context['productos'] = modelos.ProductoVenta.objects.all()
        return context