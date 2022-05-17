from django.shortcuts import render
import requests

# Create your views here.
def tienda(request):

    url = 'http://127.0.0.1:8000/productos/'
    respuesta = requests.get(url, auth=('admin', 'admin'))
    datos = respuesta.json()

    contexto = {'productos' : datos}

    return render(request,'tienda.html', contexto)

def carrito(request):
    return render(request,'carrito.html')