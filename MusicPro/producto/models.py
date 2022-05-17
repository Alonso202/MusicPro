from django.db import models
from django.utils import timezone
# Create your models here.
categoria=[
    [0, "ninguno"],
    [1, "Cuerdas"],
    [2, "Percusión"],
    [3, "Amplificadores"],
    [4, "Accesorios"]
]
class Producto (models.Model):
    serie_producto = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    codigo = models.CharField(max_length=30)
    nombre = models.CharField(max_length=100)
    fecha = models.DateTimeField(default=timezone.now)
    valor = models.IntegerField()
    imagen = models.ImageField(upload_to='img', null=True)
    categoria = models.IntegerField(choices=categoria,null=True)
    def __str__(self) :
        return self.nombre

