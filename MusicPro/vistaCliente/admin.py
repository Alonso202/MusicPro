from django.contrib import admin

# Register your models here.
from vistaCliente.models import Pedido, ProductoCarrito

admin.site.register(Pedido)
admin.site.register(ProductoCarrito)