import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "subastas.settings")
import django
django.setup()
from django.db import models
from ah.models import Producto, Cotizacion
import time, datetime
from ah.api import apiFunciones as funciones

espera = 300

print(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+': Comenzo la tarea alertas, esta programada para ejecutarse cada '+str(espera/60)+' minutos')
iteraciones =0
while True:

    iteraciones +=1
    print(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+': Comenzo la iteracion numero: '+str(iteraciones))
    time.sleep(espera)

    hora_inicio = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(str(hora_inicio) + ': Se llama a la API')

    #Iniciar API trae los datos mas actuales de la AH al JSON
    funciones.inciarAPI()
    hora_api =  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(str(hora_api) + ':Comienza el monitoreo')

    # Monitoreo todos los productos
    listaProductos = Producto.objects.all()
    for producto in listaProductos:
        print('Se esta monitoreando el precio para '+producto.nombre)
        producto = Producto.objects.get(id=producto.id)
        funciones.alertasProducto(producto)


