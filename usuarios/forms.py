from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'establecimiento', 'rut_empresa', 'direccion', 'telefono']
        widgets = {
            'direccion': forms.Textarea(attrs={'rows': 3}),
        }
