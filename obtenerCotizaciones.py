import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "subastas.settings")
import django
django.setup()
from django.db import models
from ah.models import Producto, Cotizacion
import time, datetime
from ah.api import apiFunciones as funciones

while True:

    print(str(datetime.datetime.now()) + ': Comenzo la tarea de obtener Cotizaciones')
    time.sleep(300)

    hora_inicio = datetime.datetime.now()
    print(str(hora_inicio.strftime("%Y-%m-%d %H:%M:%S")) + ': Se llama a la API de Blizzard')

    funciones.inciarAPI()

    #Guardo todos los productos que tengo en la base de datos en una lista
    listaProductos = Producto.objects.all()

    #Obtengo la cotizacion para cada unidad
    for producto in listaProductos:
        p = Producto.objects.get(id=producto.id)
        cotizacion = funciones.obtenerCotizacionProducto(p)
        hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cot = Cotizacion(None, hora, cotizacion['minimo'], cotizacion['maximo'], cotizacion['promedio'],cotizacion['cantidad'], p.id)
        cot.save()


