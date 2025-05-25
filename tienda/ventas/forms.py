from django import forms
from productos.models import Producto
from .models import Venta, DetalleVenta

class DetalleVentaForm(forms.Form):
    producto = forms.ModelChoiceField(queryset=Producto.objects.all())
    cantidad = forms.IntegerField(min_value=1)
