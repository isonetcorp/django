from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import Categoria
from .models import Proveedor
from .models import TipoGasto
from .models import Gasto

from .serializers import CategoriaSerializer
from .serializers import TipoGastoSerializer
from .serializers import ProveedorSerializer
from .serializers import GastoSerializer



class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class TipoGastoViewSet(viewsets.ModelViewSet):
    queryset = TipoGasto.objects.all()
    serializer_class = TipoGastoSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class GastoViewSet(viewsets.ModelViewSet):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer



def index(request):
    return HttpResponse("Hello World")

def contact(request, name):
    return HttpResponse(f"Alumno: Ing.{name} ")

def categorias(request):
     query = request.GET.get('nombre') 
     categorias = Categoria.objects.filter(Q(nombre__icontains=query))
     return render(request, "categorias.html", {
         "categorias": categorias
     })
     
def proveedores(request):
     query = request.GET.get('nombre') 
     proveedores = Proveedor.objects.all()
     return render(request, "proveedores.html", {
         "proveedores": proveedores
     })
         
    
#CUSTOM API
@api_view(["GET"])
def total_gastos(request):
    """
    Total de Gastos Encontrados
    """
    try:
       
        contador_gastos = Gasto.objects.count()
        return JsonResponse(
            {
                "Numero de Gastos": contador_gastos
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)
