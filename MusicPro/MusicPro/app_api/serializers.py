from rest_framework import serializers
from producto.models import Producto
from VistaEmpleados.models import Empleado
class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
class EmpleadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'
        explude= 'password'