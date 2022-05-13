
from rest_framework import serializers
from producto.models import Producto
from bodega.models import Bodega
class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ['url', 'nombre','codigo', 'valor','serie_producto','marca', 'imagen']
class BodegaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bodega
        fields = ['url','id_producto','stock']