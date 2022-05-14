from django.shortcuts import render
from rest_framework import viewsets, permissions
from bodega.models import Bodega
from producto.models import Producto
from MusicPro.app_api.serializers import BodegaSerializer,ProductoSerializer
# Create your views here.
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticated]
class BodegaViewSet(viewsets.ModelViewSet):
    queryset = Bodega.objects.all()
    serializer_class = BodegaSerializer
    permission_classes = [permissions.IsAuthenticated]
