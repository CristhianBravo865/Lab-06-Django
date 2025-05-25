from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('', views.lista_productos, name='lista_productos'),
]
