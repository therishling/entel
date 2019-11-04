from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from apps.ventas import models as modelo

from apps.ventas.forms import CrearUsuario, ModificarUsuario
# Register your models here.

class UserAdmin(BaseUserAdmin):
    form = ModificarUsuario
    add_form = CrearUsuario
    
    list_display = ('correo', 'admin')
    list_filter = ('admin',)
    fieldsets = ((None, {'fields': ('correo', 'password', )}),('Informacion Personal',{'fields': ('nombre','apellido_paterno','apellido_materno','fecha_nacimiento')}),('Permisos',{'fields': ('admin','staff','active')}),)

    add_fieldsets = ((None, {
        'classes':('wide',),
        'fields': ('username','correo','password1','password2')
    }),)

    search_fields = ('correo',)
    ordering = ('correo',)
    filter_horizontal =()




admin.site.register(modelo.Producto)
admin.site.register(modelo.ProductoVenta)
admin.site.register(modelo.Vendedor, UserAdmin)
admin.site.register(modelo.Venta)
