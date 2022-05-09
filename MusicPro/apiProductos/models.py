from django.db import models
from mailbox import NoSuchMailboxError
from django.utils import timezone
# Create your models here.
class Producto (models.Model):
    serie_producto = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    codigo = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    fecha = models.DateTimeField(default=timezone.now)
    valor = models.IntegerField()
    imagen = models.ImageField(upload_to='img', null=True)
    def __str__(self) :
        return self.nombre
   
