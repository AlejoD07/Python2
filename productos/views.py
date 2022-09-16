from asyncio.windows_events import NULL
from django.shortcuts import render
from .models import Producto
# Create your views here.
def verProductos(request, id=NULL):
    listaProductos = Producto.objects.all()
    context={
        'productos':listaProductos,
    }
    return render(request, 'productos/producto.html',context)