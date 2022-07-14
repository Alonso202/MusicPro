from django.shortcuts import redirect, render
import requests
from rest_framework import viewsets
from django.contrib.auth import authenticate, login
# Create your views here.
def index(request):
    
    if request.method=='POST': 
        usu = request.POST['usu']
        passw = request.POST['passw']
        user = authenticate(request, username=usu, password=passw)
        if user is not None:
            login(request, user)
            if user.groups.filter(name__in=['Bodeguero']):
                return render(request, 'homeBod.html')
            if user.groups.filter(name__in=['Vendedor']):
                return render(request, 'homeVend.html')
            if user.groups.filter(name__in=['Contador']):
                return render(request, 'homeCon.html')                        
        else:
            return redirect('http://127.0.0.1:8000/tienda')
    return render(request,'index.html')
            
    
def homeBod(request):
    url = 'http://127.0.0.1:8000/api/pedidos/'
    respuesta = requests.get(url, auth=('admin', 'admin'))
    datos = respuesta.json()
    contexto = {'pedidos' : datos}
    return render(request,'homeBod.html',contexto)

def homeCon(request):
    url = 'http://127.0.0.1:8000/api/pedidos/'
    respuesta = requests.get(url, auth=('admin', 'admin'))
    datos = respuesta.json()
    contexto = {'pedidos' : datos}
    return render(request,'homeCon.html',contexto)
    
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
def despachadoCliente(request,id):
    url= "http://127.0.0.1:8000/api/pedidos/"+str(id)+'/'
    json = {"estado" : "Enviado a Cliente"}
    response = requests.patch(url, auth=('admin','admin'), data = json)
    datos= response.json()
    return redirect("/pedidos")

def despachado(request,id):
    url= "http://127.0.0.1:8000/api/pedidos/"+str(id)+'/'
    json = {"estado" : "Despacho a Vendedor"}
    response = requests.patch(url, auth=('admin','admin'), data = json)
    datos= response.json()
    return redirect("/bodeguero")

def recibido(request,id):
    url= "http://127.0.0.1:8000/api/pedidos/"+str(id)+'/'
    json = {"estado" : "Recibido a Cliente"}
    response = requests.patch(url, auth=('admin','admin'), data = json)
    datos= response.json()
    return redirect("/contador")
<<<<<<< HEAD

def pagado(request,id):
    url= "http://127.0.0.1:8000/api/pedidos/"+str(id)+'/'
    json = {"estado" : "Pagado"}
    response = requests.patch(url, auth=('admin','admin'), data = json)
    datos= response.json()
    return redirect("/tienda")
=======
def authLogin(request):
    if request.method=='POST': 
        usu = request.POST['usu']
        passw = request.POST['passw']
        print(usu,passw)
        user = authenticate(request, username=usu, password=passw)
        if user is not None:
            login(request, user)
            
            if user.group == 'Bodeguero':
                return render(request, 'http://127.0.0.1:8000/bodeguero')
            if user.group == 'Vendedor':
                return render(request, 'http://127.0.0.1:8000/vendedor')
            if user.group == 'Contador':
                return render(request, 'http://127.0.0.1:8000/contador')                        
        else:
            return redirect('http://127.0.0.1:8000/tienda')
>>>>>>> b46e5db94bbe6be544a6821462105d59a2a3d512
