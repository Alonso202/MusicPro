from rest_framework import serializers
from producto.models import Producto
from bodega.models import Bodega
from VistaEmpleados.models import Empleado
class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ['url', 'nombre','codigo', 'valor','serie_producto','marca', 'imagen']
class BodegaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bodega
        fields = ['url','id_producto','stock']
class EmpleadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Empleado
        fields = ['url','username','email', 'puesto','nombre','rut']