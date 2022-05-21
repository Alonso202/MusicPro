from django.shortcuts import render
from rest_framework import viewsets, permissions
from producto.models import Producto
from VistaEmpleados.models import Empleado
from MusicPro.app_api import serializers
# Create your views here.
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = serializers.ProductoSerializer
    permission_classes = [permissions.IsAuthenticated]
class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = serializers.EmpleadoSerializer
    permission_classes = [permissions.IsAuthenticated]