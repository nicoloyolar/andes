from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'establecimiento', 'rut_empresa', 'direccion', 'telefono']
        widgets = {
            'direccion': forms.Textarea(attrs={'rows': 3}),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio']
        widgets = {
            'direccion': forms.Textarea(attrs={'rows': 3}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'establecimiento', 'rut_empresa', 'direccion', 'telefono']  