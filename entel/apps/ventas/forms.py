from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from apps.ventas import models as modelo


    
class CrearUsuario(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = modelo.Vendedor
        fields = ('nombre','apellido_paterno','apellido_materno','fecha_nacimiento','correo','password1')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError("Contraseñas no coinciden")
        return password2
    
    def save(self, commit=True):
        usuario = super(CrearUsuario, self).save(commit=False)
        usuario.set_password(self.cleaned_data["password1"])
        
        if commit:
            
            usuario.save()
        return usuario

class ModificarUsuario(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = modelo.Vendedor
        fields = ('nombre','apellido_paterno','apellido_materno','fecha_nacimiento','correo','password',)
        
    
    def clean_password(self):
        return self.initial['password']


class ProductoForm(forms.ModelForm):
    class Meta:
        model = modelo.Producto
        fields = ('nombre_producto','precio',)



class VentaForms(forms.ModelForm):
    class Meta:
        model = modelo.Venta
        fields = ('vendedor','fecha','producto','comentarios','total')
        widgets = {
            'producto': forms.SelectMultiple(attrs={"class":"pene"}),          
        }