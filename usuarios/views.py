from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import ClienteForm
from .models import Cliente

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
    return render(request, 'usuarios/ingresar_venta.html')

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

def venta_cliente_view(request):
    return render(request, 'usuarios/venta_cliente.html')