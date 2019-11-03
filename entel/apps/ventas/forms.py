from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from apps.ventas import models as modelo

class PersonaForms(forms.ModelForm):
    class Meta:
        model = modelo.Vendedor
        fields = [
            'nombre',
            'apellido',
            'edad',
            'telefono',
            'email',
            'domicilio',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'edad': 'Edad',
            'Telefono': 'Telefono',
            'email': 'Email',
            'domicilio': 'Domicilio',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={"class":"form-control"}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'edad': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'domicilio': forms.TextInput(attrs={'class':'form-control'}),
        }
    
class CrearUsuario(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password1 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = modelo.Vendedor
        fields = ('nombre','apellido_paterno','apellido_materno','fecha_nacimiento','usuario','password')