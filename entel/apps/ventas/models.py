from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.

class ManejadorUsuario(BaseUserManager):

    def create_user(self, correo, password = None):
        if not correo:
            raise ValueError('Usuarios deben tener un correo valido.')
        
        usuario = self.model(correo = self.normalize_email(correo), )
        usuario.set_password(password)
        usuario.save(using = self._db)
        return usuario
    
    def create_staffuser(self, correo, password):
        usuario = self.create_user(correo, password=password)
        usuario.staff = True
        usuario.save(using = self._db)
        return usuario

    def create_superuser(self, correo, password):
        usuario = self.create_user(correo, password=password)
        usuario.staff = True
        usuario.admin = True
        usuario.save(using = self._db)
        return usuario



class Vendedor(AbstractBaseUser):
    nombre = models.CharField(max_length=200)
    apellido_paterno = models.CharField(max_length=80)
    apellido_materno = models.CharField(max_length=80)
    fecha_nacimiento = models.DateField(null = True)
    correo = models.EmailField(verbose_name='correo',max_length=100, unique=True)
    is_vendedor = models.BooleanField(default = True)
    active = models.BooleanField(default = True)
    staff = models.BooleanField(default = False)
    admin = models.BooleanField(default = False)

    objects = ManejadorUsuario()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.nombre + ' ' + self.apellido_paterno + ' ' + self.apellido_materno
    
    def get_short_name(self):
        return self.nombre
    
    def has_perm(self, perm, obj = None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido_paterno + ' ' + self.apellido_materno
    

class Venta(models.Model):
    vendedor = models.ForeignKey(Vendedor, null=True, blank=True, on_delete=models.CASCADE)
    fecha = models.DateField()
    comentarios = models.TextField()

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100)
    precio = models.IntegerField()

class ProductoVenta(models.Model):
    venta = models.ForeignKey(Venta, null=True, blank=True, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, null=True, blank=True, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    total = models.IntegerField(default=0)