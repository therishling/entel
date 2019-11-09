from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse,reverse_lazy
from apps.ventas import models as modelos
from apps.ventas import forms as formularios
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
def index(request):
    user = request.user
    if user.admin:
        return render(request, 'dashboard/index.html')
    return render(request, 'dashboard/index.html')

class CrearUsuario(SuccessMessageMixin, CreateView):
    model = modelos.Vendedor
    form_class = formularios.CrearUsuario
    template_name = 'dashboard/admin/crearvendedor.html'
    success_message = 'Usuario registrado correctamente'
    success_url = reverse_lazy('crear usuario')