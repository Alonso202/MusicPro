from rest_framework import serializers
from producto.models import Producto
from VistaEmpleados.models import Empleado

from vistaCliente.models import Pedido, ProductoCarrito

class ProductoCarritoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductoCarrito
        fields = [ 'id', 'marca', 'nombre', 'valor', 'imagen']

class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    
    productoCarrito = ProductoCarritoSerializer(read_only=True, many=True)

    class Meta:
        model = Pedido
        fields = ['url', 'id', 'nombreUsuario', 'valorTotal', 'productoCarrito', 'estado']


class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ['url','id' ,'nombre','codigo', 'valor','serie_producto','marca', 'imagen', 'categoria', 'fecha', 'stock']
class EmpleadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'
        explude= 'password'