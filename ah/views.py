from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from ah.graficas.GraficasFunciones import Graficador
from django.db import models
from ah.models import Producto, Cotizacion
# Create your views here.

def test(request):

    Rosaluz = Producto.objects.get(id=124105)
    g = Graficador()
    g.obtenerGraficaEvolucion(Rosaluz)
    imagen = '/media/graficas/'+Rosaluz.nombre+'.svg'

    return render(request, 'test.html', {'imagen':imagen})

def verGrafica(request, producto):
    return HttpResponse('Todos putos')