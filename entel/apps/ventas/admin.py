from django.contrib import admin
from apps.ventas import models as modelo
# Register your models here.

admin.site.register(modelo.Producto)
admin.site.register(modelo.ProductoVenta)
admin.site.register(modelo.Vendedor)
admin.site.register(modelo.Venta)
