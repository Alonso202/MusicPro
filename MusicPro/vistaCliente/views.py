from django.shortcuts import render, redirect
import requests

# Create your views here.
def tienda(request):

    url = 'http://127.0.0.1:8000/api/productos/'
    respuesta = requests.get(url, auth=('admin', 'admin'))
    datos = respuesta.json()

    contexto = {'productos' : datos}

    return render(request,'tienda.html', contexto)

from vistaCliente.models import Pedido, ProductoCarrito

def carrito(request):
    
    url = 'http://127.0.0.1:8000/api/productos/'
    respuesta = requests.get(url, auth=('admin', 'admin'))
    datos = respuesta.json()

    if request.method=="POST":
        nombreUsuario = request.POST['nombreUsuario']
        valorTotal = request.POST['valorTotal']
        productos = request.POST['productosCarrito']
        estado = request.POST['estado']
        
        pedido = Pedido(nombreUsuario = nombreUsuario, valorTotal=valorTotal, estado=estado)
        pedido.save()

        arregloProductos = productos.split()

        for i in datos:
            
            if(str(i['id']) in arregloProductos):
                print('el producto esta')
                productoCarrito = ProductoCarrito(marca=i['marca'], nombre=i['nombre'], valor=i['valor'], imagen=i['imagen'])
                productoCarrito.save()
                pedido.productoCarrito.add(productoCarrito)

        return redirect('tienda')


    return render(request,'carrito.html')