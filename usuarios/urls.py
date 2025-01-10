from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view, name='login'),
    path('administracion/', listar_productos_view, name='administracion'),
    path('home/', home_view, name='home'),
    path('ventas/', ventas_view, name='ventas'),
    path('buscar-clientes/', buscar_clientes, name='buscar-clientes'),
    path('editar-cliente/<int:id>/', editar_cliente_view, name='editar-cliente'),
    path('ingresar-venta/', ingresar_venta_view, name='ingresar-venta'),
    path('crear-cliente/', crear_cliente_view, name='crear-cliente'),
    path('crear-producto/', crear_producto_view, name='crear-producto'),
    path('listar-clientes/', lista_clientes_view, name='listar-clientes'),
    path('eliminar-cliente/<int:cliente_id>/', eliminar_cliente_view, name='eliminar-cliente'),
    path('eliminar_producto/<int:producto_id>/', eliminar_producto_view, name='eliminar_producto'),
    path('venta_cliente/<int:cliente_id>/', venta_cliente_view, name='venta_cliente'),
]
