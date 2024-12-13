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
    nombre = models.CharField(max_length=100)
    establecimiento = models.CharField(max_length=100)
    rut_empresa = models.CharField(max_length=20, unique=True)
    direccion = models.TextField(null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.establecimiento})"
