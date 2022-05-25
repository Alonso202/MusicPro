"""MusicPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from MusicPro.app_api import views
from VistaEmpleados.views import index,homeVendViewSet,homeBod,homeCon,stockProd,pedidos,aceptar,rechazar,despachado
from django.conf import settings
from django.conf.urls.static import static

from vistaCliente.views import tienda, carrito

router = routers.DefaultRouter()

router.register(r'pedidos', views.PedidoViewSet)
#router.register(r'productoCarrito', views.ProductoCarritoViewSet)

router.register(r'productos', views.ProductoViewSet)
router.register(r'empleados',views.EmpleadoViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth', include('rest_framework.urls',namespace='rest_framework')),
    path('login', index, name = "login"),
    path('tienda', tienda, name='tienda'),
    path('carrito', carrito, name='carrito'),
    path('vendedor',homeVendViewSet.mostrar,name='vendedor'),
    path('bodeguero',homeBod,name='homeBod' ),
    path('contador',homeCon,name= 'homeCon' ),
    path('vendedor/productos',stockProd,name= 'stockProd' ),
    path('pedidos',pedidos,name= 'pedidos' ),
    path('aceptar/<int:id>/',aceptar,name="aceptar"),
    path('rechazar/<int:id>/',rechazar,name="rechazar"),
    path('despachado/<int:id>/',despachado,name="despachado")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)