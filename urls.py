from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('distribucion/', include('app_distribucion.urls')),
    path('usuarios/', include('usuarios.urls')),
]
