from django.urls import path
from .views import login_view, home_view, ventas_view, ingresar_venta_view, crear_cliente_view, lista_clientes_view

urlpatterns = [
    path('', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('ventas/', ventas_view, name='ventas'),
    path('ingresar-venta/', ingresar_venta_view, name='ingresar-venta'),
    path('crear-cliente/', crear_cliente_view, name='crear-cliente'),
    path('listar-clientes/', lista_clientes_view, name='listar-clientes'),
]
