from django.shortcuts import render
from rest_framework import viewsets, permissions
from producto.models import Producto
from VistaEmpleados.models import Empleado
from MusicPro.app_api import serializers
# Create your views here.
from vistaCliente.models import Pedido, ProductoCarrito

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = serializers.PedidoSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductoCarritoViewSet(viewsets.ModelViewSet):
    queryset = ProductoCarrito.objects.all()
    serializer_class = serializers.ProductoCarritoSerializer
    permission_classes = [permissions.IsAuthenticated]



class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = serializers.ProductoSerializer
    permission_classes = [permissions.IsAuthenticated]
class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = serializers.EmpleadoSerializer
    permission_classes = [permissions.IsAuthenticated]
