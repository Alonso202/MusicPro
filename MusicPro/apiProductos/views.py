from django.shortcuts import render
from rest_framework import viewsets,permissions
from apiProductos.serializers import ProductoSerializer
from apiProductos.models import Producto
# Create your views here.
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticated]