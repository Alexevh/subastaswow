import pygal
import csv
import operator
from matplotlib import pyplot as plt
from datetime import datetime
import os, re
#from clases.productos import Producto
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "subastas.settings")
import django
django.setup()
from django.db import models
from ah.models import Producto, Cotizacion

class Graficador():

    def obtenerGraficaEvolucion(self, producto):
        formatoFecha = "%H:%M:%S"
        minimos = []
        maximos = []
        fechas = []
        promedios = []

    # Abrimos el CSV como fichero
        with open('ah/resultados/Rosaluz.csv', encoding='utf8') as f:
            reader = csv.reader(f)
        # Recorro todaslas lineas del CSV
            for row in reader:
                fechas.append(str(row[0]))
                maximos.append(float(row[2]))
                minimos.append(float(row[1]))
                promedios.append(float(row[3]))




    # Dibujo la grafica de lineas
        line_chart = pygal.Line()
        line_chart.title = ('Evolucion de '+producto.nombre)
        line_chart.x_labels =  fechas
        line_chart.add('Maximos', maximos)
        line_chart.add('Minimos', minimos)
        line_chart.add('Promedio', promedios)
        line_chart.render_to_file('media/graficas/Rosaluz.svg')


