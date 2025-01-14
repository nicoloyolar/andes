from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = [
        ('ADMIN', 'Administrador'),
        ('VENDEDOR', 'Vendedor'),
    ]
    rol = models.CharField(max_length = 10, choices = ROLES, default = 'VENDEDOR')

    def administrador(self):
        return self.rol == 'ADMIN'

    def vendedor(self):
        return self.rol == 'VENDEDOR'

class Cliente(models.Model):
    nombre              = models.CharField(max_length=100)
    establecimiento     = models.CharField(max_length=100)
    rut_empresa         = models.CharField(max_length=20, unique=True)
    direccion           = models.TextField(null=True, blank=True)
    telefono            = models.CharField(max_length=20, null=True, blank=True)
    fecha_registro      = models.DateTimeField(auto_now_add=True)
    deuda               = models.PositiveIntegerField(default=0)  

    def __str__(self):
        return f"{self.nombre} ({self.establecimiento})"
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)  
    precio = models.PositiveIntegerField()  
    stock = models.PositiveIntegerField(default=0)  

    def __str__(self):
        return self.nombre
    
class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20)
    fecha = models.DateField(auto_now_add=True)

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()  
    subtotal = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad} grs - ${self.subtotal}"
