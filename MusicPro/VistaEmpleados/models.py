from django.db import models
opciones_puesto = [
    [0, "Administrador"],
    [1, "Bodeguero"],
    [2, "Vendedor"],
    [3, "Contador"]
]
# Create your models here.
class Empleado (models.Model):
    rut= models.CharField(max_length=9)
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    puesto = models.IntegerField(choices= opciones_puesto)
    def __str__(self):
        return self.username

