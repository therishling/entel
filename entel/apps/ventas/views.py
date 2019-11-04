from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse,reverse_lazy
# Create your views here.
def index(request):
    user = request.user
    if user.admin:
        return HttpResponse('Soy el dashboard admin.')
    return HttpResponse('Soy el dashboard.')