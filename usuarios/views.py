from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import ClienteForm
from .models import Cliente
from django.http import JsonResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'Por favor, completa todos los campos.')
            return render(request, 'usuarios/login.html')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Has iniciado sesión con éxito.')
            return redirect('home')  
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')

    return render(request, 'usuarios/login.html')

def home_view(request):
    return render(request, 'usuarios/home.html')

def ventas_view(request):
    return render(request, 'usuarios/ventas.html')

def ingresar_venta_view(request):
    
    query = request.GET.get('search', '')  
    clientes = Cliente.objects.filter(nombre__icontains=query)  
    
    return render(request, 'usuarios/ingresar_venta.html', {'clientes': clientes})

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

def venta_cliente_view(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    return render(request, 'usuarios/venta_cliente.html', {'cliente': cliente})

def buscar_clientes(request):
    query = request.GET.get('search', '') 
    clientes = Cliente.objects.filter(establecimiento__icontains=query)  
    clientes_data = list(clientes.values('id', 'nombre', 'establecimiento'))  

    return JsonResponse(clientes_data, safe=False)