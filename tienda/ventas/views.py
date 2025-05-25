from django.shortcuts import render, redirect
from django.forms import formset_factory
from .forms import DetalleVentaForm
from .models import Venta, DetalleVenta

def registrar_venta(request):
    DetalleVentaFormSet = formset_factory(DetalleVentaForm, extra=1, can_delete=True)

    if request.method == 'POST':
        formset = DetalleVentaFormSet(request.POST)
        if formset.is_valid():
            venta = Venta.objects.create()
            for form in formset:
                if form.cleaned_data:
                    producto = form.cleaned_data['producto']
                    cantidad = form.cleaned_data['cantidad']
                    DetalleVenta.objects.create(venta=venta, producto=producto, cantidad=cantidad)
            return redirect('ventas:lista_ventas')
    else:
        formset = DetalleVentaFormSet()

    return render(request, 'ventas/registrar_venta.html', {'formset': formset})
def lista_ventas(request):
    ventas = Venta.objects.all().order_by('-fecha')
    return render(request, 'ventas/lista_ventas.html', {'ventas': ventas})