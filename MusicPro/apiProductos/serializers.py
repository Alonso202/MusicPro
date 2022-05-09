
from rest_framework import serializers
from apiProductos.models import Producto

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ['url', 'nombre','codigo', 'valor','serie_producto','marca', 'imagen']