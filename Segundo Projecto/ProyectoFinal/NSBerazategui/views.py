from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "NSBerazategui/index.html")

def contacto(request):
    return render(request, "NSBerazategui/contacto.html")

def nuestros_servicios(request):
    return render(request, "NSBerazategui/nuestros_servicios.html")

def quienes_somos(request):
    return render(request, "NSBerazategui/quienes_somos.html")