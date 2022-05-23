from django.db import models
# Create your models here.

class ProductoCarrito (models.Model):
    marca = models.CharField(max_length=30)
    nombre = models.CharField(max_length=100)
    valor = models.IntegerField()
    imagen = models.CharField(max_length=100)
    def __str__(self) :
        return self.nombre

class Pedido (models.Model):
    nombreUsuario = models.CharField(max_length=100)
    valorTotal = models.IntegerField()
    productoCarrito = models.ManyToManyField(ProductoCarrito)
    estado = models.CharField(max_length=20)

    def __str__(self):
        return  'Pedido de '+ self.nombreUsuario