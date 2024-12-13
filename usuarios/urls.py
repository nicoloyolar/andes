from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('ventas/', ventas_view, name='ventas'),
    path('ingresar-venta/', ingresar_venta_view, name='ingresar-venta'),
    path('crear-cliente/', crear_cliente_view, name='crear-cliente'),
    path('listar-clientes/', lista_clientes_view, name='listar-clientes'),
    path('venta-cliente/', venta_cliente_view, name='venta-cliente'),
]
