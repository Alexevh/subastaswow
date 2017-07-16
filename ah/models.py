from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Producto(models.Model):

    nombre = models.CharField(max_length=200, unique=True)
    id =  models.PositiveIntegerField(primary_key=True)
    umbral = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre




class Cotizacion(models.Model):

    fecha = models.DateTimeField()
    minimo = models.FloatField()
    maximo = models.FloatField()
    promedio = models.FloatField()
    cantidad = models.PositiveIntegerField()
    Producto = models.ForeignKey(Producto)

    def __str__(self):

        return self.Producto.nombre +' : '+ str(self.fecha)

