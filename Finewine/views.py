from django.shortcuts import render
def home(request):
    return render(request, "home.html")

def verProducto(request):
    return render(request, 'producto.html')

def verNosotros(request):
        return render(request, 'nosotros.html')

def verContactanos(request):
        return render(request, 'contactanos.html')