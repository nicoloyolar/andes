from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return render(request, 'usuarios/login.html')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            pass

    return render(request, 'usuarios/login.html')

def logout_view(request):
    logout(request)  
    return redirect('login') 

def home_view(request):
    query = request.GET.get('search', '')  
    clientes = Cliente.objects.filter(nombre__icontains=query)  
    
    return render(request, 'usuarios/home.html', {'clientes': clientes})


def ventas_view(request):
    return render(request, 'usuarios/ventas.html')

def ingresar_venta_view(request):
    
    query = request.GET.get('search', '')  
    clientes = Cliente.objects.filter(nombre__icontains=query)  
    
    return render(request, 'usuarios/ingresar_venta.html', {'clientes': clientes})

### MANTENEDOR CLIENTES

def crear_cliente_view(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar-clientes')
    else:
        form = ClienteForm()

    return render(request, 'usuarios/crear_cliente.html', {'form': form})

def lista_clientes_view(request):
    clientes = Cliente.objects.all()
    
    return render(request, 'usuarios/listar_clientes.html', {'clientes': clientes})

def eliminar_cliente_view(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    
    if request.method == 'POST':
        cliente.delete()
        return redirect('listar-clientes')  

    return render(request, 'usuarios/eliminar_cliente.html', {'cliente': cliente})

###### MANTENEDOR PRODUCTOS

def crear_producto_view(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administracion')  
    else:
        form = ProductoForm()

    return render(request, 'usuarios/crear_producto.html', {'form': form})
    
def listar_productos_view(request):
    productos = Producto.objects.all()

    return render(request, 'usuarios/administracion.html', {'productos': productos})

def eliminar_producto_view(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return JsonResponse({'success': True})

###### MANTENEDOR VENTAS

def venta_cliente_view(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    productos = Producto.objects.all()
    if request.method == "POST":
        pass
    return render(request, 'usuarios/venta_cliente.html', {'cliente': cliente, 'productos': productos})

def buscar_clientes(request):
    query = request.GET.get('search', '') 
    clientes = Cliente.objects.filter(establecimiento__icontains=query)  
    clientes_data = list(clientes.values('id', 'nombre', 'establecimiento'))  

    return JsonResponse(clientes_data, safe=False)

def editar_cliente_view(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()  
            return redirect('listar-clientes')
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'usuarios/editar_cliente.html', {'form': form})

##### MODULO VENTAS

def venta_cliente_view(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    productos = Producto.objects.all()

    if request.method == 'POST':
        productos_seleccionados = []
        cantidades = []
        total = 0

        for producto in productos:
            cantidad = float(request.POST.get(f'cantidades_{producto.id}', 0))
            total_producto = float(request.POST.get(f'total_producto_{producto.id}', 0))

            if cantidad > 0:
                productos_seleccionados.append(producto)
                cantidades.append(cantidad)
                total += total_producto  

        venta = Venta(cliente=cliente, total=total, estado=request.POST['estado'])
        venta.save()

        for i, producto in enumerate(productos_seleccionados):
            detalle = DetalleVenta(venta=venta, producto=producto, cantidad=cantidades[i], subtotal=cantidades[i] * producto.precio / 1000)
            detalle.save()

        return redirect('ventas')

    return render(request, 'usuarios/venta_cliente.html', {'cliente': cliente, 'productos': productos})

def ventas_view(request):
    ventas = Venta.objects.all()  
    for venta in ventas:
        print(venta.total) 
    return render(request, 'usuarios/ventas.html', {'ventas': ventas})