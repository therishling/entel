from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse,reverse_lazy
from apps.ventas import models as modelos
from apps.ventas import forms as formularios
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin



# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')


# Funcionalidades ADMIN

class CrearUsuario(UserPassesTestMixin, SuccessMessageMixin, CreateView):

    model = modelos.Vendedor
    form_class = formularios.CrearUsuario
    template_name = 'dashboard/admin/formvendedor.html'
    success_message = 'Usuario registrado correctamente'
    success_url = reverse_lazy('crear usuario')
    
    def test_func(self):
        user = self.request.user
        return user.admin
    
    def handle_no_permission(self):
        return redirect('dashboard')

class ListarUsuarios(UserPassesTestMixin, SuccessMessageMixin, ListView):
    model = modelos.Vendedor
    template_name = 'dashboard/admin/listausuario.html'
    context_object_name = 'usuarios'

    def test_func(self):
        user = self.request.user
        return user.admin
    
    def handle_no_permission(self):
        return redirect('dashboard')
        

    
class ModificarUsuarioAdmin(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = modelos.Vendedor
    form_class = formularios.ModificarUsuario
    template_name = 'dashboard/admin/formvendedor.html'
    success_url = reverse_lazy('listar usuario')
    context_object_name = 'usuario'
    def test_func(self):
        user = self.request.user
        return user.admin
    
    def handle_no_permission(self):
        return redirect('dashboard')

class EliminarUsuario(UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = modelos.Vendedor
    template_name = 'dashboard/admin/listausuario.html'
    success_url = reverse_lazy('listar usuario')
    context_object_name = 'usuario'
    def test_func(self):
        user = self.request.user
        return user.admin
    
    def handle_no_permission(self):
        return redirect('dashboard')
 