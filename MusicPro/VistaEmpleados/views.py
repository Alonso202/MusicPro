from django.shortcuts import redirect, render,get_object_or_404
import requests
from rest_framework import viewsets
from producto.models import Producto
from MusicPro.app_api.serializers import ProductoSerializer
# Create your views here.
def index(request):
    url = 'http://127.0.0.1:8000/empleados/'
    respuesta = requests.get(url, auth=('admin', 'admin'))
    datos = respuesta.json()
    

    if request.method=='POST': 
        usuario_form = ProductoSerializer(request.POST)
        if usuario_form.is_valid():
            if(datos.puesto==1):
                return redirect(request,'homeBod.html')
            elif(datos.puesto==2):
                return redirect(request,'homeVend.html')
            elif(datos.puesto==3):
                return redirect(request,'homeCon.html')
            usuario_form.save()    #save() reemplaza al insert
            return redirect('index')
        
    return render(request,'index.html')
def homeBod(request):
    return render(request,'homeBod.html')
def homeCon(request):
    return render(request,'homeCon.html')

class homeVendViewSet(viewsets.ViewSet):
    def mostrar(request):
        url = 'http://127.0.0.1:8000/productos/'
        respuesta = requests.get(url, auth=('admin', 'admin'))
        datos = respuesta.json()
        contexto = {'productos' : datos}
        return render(request,'homeVend.html',contexto)
    def modificar(request, nombre):

        producto = get_object_or_404(Producto, nombre=nombre)

        data = {
            'form': ProductoSerializer(instance=producto)
        }

        if request.method == 'PATCH':
            formulario = ProductoSerializer(data=request.patch, instance=producto, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                return redirect(to="listado")
            data["form"] = formulario 


        return render(request, 'http://127.0.0.1:8000/vendedor#productos', data)  