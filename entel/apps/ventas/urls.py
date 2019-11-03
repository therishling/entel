from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from apps.ventas.views import index
urlpatterns = [
    path('dashboard/', login_required(index) ,name='dashboard'),
]
