from django.db import models
from producto.models import Producto
# Create your models here.
class Bodega (models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)