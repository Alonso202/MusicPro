from django.shortcuts import redirect, render,get_object_or_404
import requests
from rest_framework import viewsets
from MusicPro.app_api import serializers
# Create your views here.
def index(request):
    return render(request,'index.html')
    
def homeBod(request):
    url = 'http://127.0.0.1:8000/api/pedidos/'
    respuesta = requests.get(url, auth=('admin', 'admin'))
    datos = respuesta.json()
    contexto = {'pedidos' : datos}
    return render(request,'homeBod.html',contexto)

def homeCon(request):
    return render(request,'homeCon.html')
def stockProd(request):
    return render(request,'stockProd.html')


def pedidos(request):
        url = 'http://127.0.0.1:8000/api/pedidos/'
        respuesta = requests.get(url, auth=('admin', 'admin'))
        datos = respuesta.json()
        contexto = {'pedidos' : datos}
        return render(request,'pedidos.html',contexto)
class homeVendViewSet(viewsets.ViewSet):
    def mostrar(request):
        url = 'http://127.0.0.1:8000/api/productos/'
        respuesta = requests.get(url, auth=('admin', 'admin'))
        datos = respuesta.json()
        contexto = {'productos' : datos}
        return render(request,'homeVend.html',contexto)

def aceptar(request,id):
    url= "http://127.0.0.1:8000/api/pedidos/"+str(id)+'/'
    json = {"estado" : "Aprobado"}
    response = requests.patch(url, auth=('admin','admin'), data = json)
    datos= response.json()
    return redirect("/pedidos")

def rechazar(request,id):
    url= "http://127.0.0.1:8000/api/pedidos/"+str(id)+'/'
    json = {"estado" : "Rechazado"}
    response = requests.patch(url, auth=('admin','admin'), data = json)
    datos= response.json()
    return redirect("/pedidos")


def despachado(request,id):
    url= "http://127.0.0.1:8000/api/pedidos/"+str(id)+'/'
    json = {"estado" : "Despachado"}
    response = requests.patch(url, auth=('admin','admin'), data = json)
    datos= response.json()
    return redirect("/bodeguero")