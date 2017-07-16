import json
import requests
import ast
import ah.busquedas.busquedas as b
import datetime
import ah.correos.funciones as f
#from ah.clases.productos import Producto
from ah.config import config as c

def inciarAPI():

    #Llamada a la API de la casa de subastas
    llamada = 'https://us.api.battle.net/wow/auction/data/drakkari?locale=en_US&apikey='+c['API-KEY']
    #genero una variable de texto
    ficheroJson = ''
    try:
        #Obtengo una respuesta de la URL
        response = requests.get(llamada)



    #Paso a texto la respuesta
        resultado = response.text
    #Le quito las ';' por que no me sirven para pasar a python
        resultado = resultado.replace(";", "")
    #Convierto en json el resultado
        resultado = json.loads(resultado)

    #El resultado me trae un diccionario que consta de una sola clave con un valor que es un diccionario
        lista = resultado['files']
    #Del diccionario solo me interesa la URL de donde voy a bajar el JSON de Blizzard
        for fila in lista:
         ficheroJson = fila['url']

    #Con la URL obtenida de blizzar obtengo el json
        response2 = requests.get(ficheroJson)
    #Esta parte guarda el json propiamente
        data = json.loads(response2.text)

    #Voy a guardar el JSON en un temporal y registro la llamada
        with open('ah/resultados/temporal.json', 'w') as temporal:

            json.dump(data, temporal)
            with open('ah/logs/registro.txt', 'a') as registro:
                hora = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                registro.write(str(hora) + ' : Se llamo a la API para traer el JSON ' + '\n')
    except:
        with open('ah/logs/registro.txt', 'a') as registro:
            hora = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            registro.write(str(hora) + ' : Error en la llamada a la API para traer el JSON ' + '\n')


def monitorearProductos(producto):

    p = producto

    with open('ah/resultados/'+p.nombre+'.csv', 'a') as fichero:
        with open('ah/resultados/temporal.json') as json_data:
            d = json.load(json_data)
            resultadoX = b.buscarObjeto(d, producto.id)
            #print(resultadoX)
            maximo = round(resultadoX['maximo'],2)
            minimo = round(resultadoX['minimo'],2)
            promedio = round(resultadoX['promedio'], 2)

            if minimo <= producto.umbral and minimo !=0:
                hacia = c['SMTP_DESTINO']
                desde = c['STMP_ORIGEN']
                asunto = 'ALERTA : Posible oportunidad de ' + producto.nombre
                mensaje = 'En la ultima consulta se registro el valor de {0} para el producto {1}, el promedio del articulo es de {3} y el maximo es de {2}: '
                f.enviarMensaje(desde, hacia, asunto, mensaje.format(minimo, producto, maximo, promedio))


            #hora =datetime.datetime.now().strftime("%H:%M:%S")
            hora = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            fichero.write(str(hora)+','+str(minimo)+','+str(maximo)+','+str(promedio)+'\n')

def alertasProducto(producto):
    p = producto
    with open('ah/resultados/temporal.json') as json_data:
        d = json.load(json_data)
        resultadoX = b.buscarObjeto(d, producto.id)
        # print(resultadoX)
        maximo = round(resultadoX['maximo'], 2)
        minimo = round(resultadoX['minimo'], 2)
        promedio = round(resultadoX['promedio'], 2)

        if minimo <= producto.umbral and minimo != 0:
            hacia = c['SMTP_DESTINO']
            desde = c['STMP_ORIGEN']
            asunto = 'ALERTA : Posible oportunidad de ' + producto.nombre
            mensaje = 'En la ultima consulta se registro el valor de {0} para el producto {1}, el promedio del articulo es de {3} y el maximo es de {2}: '
            f.enviarMensaje(desde, hacia, asunto, mensaje.format(minimo, producto, maximo, promedio))

def obtenerCotizacionProducto(producto):

    with open('ah/resultados/temporal.json') as json_data:
        d = json.load(json_data)
        resultadoX = b.buscarObjeto(d, producto.id)
            # print(resultadoX)

        cantidad = resultadoX['cantidad']
        maximo = round(resultadoX['maximo'], 2)
        minimo = round(resultadoX['minimo'], 2)
        promedio = round(resultadoX['promedio'], 2)
        cotizacion = {'cantidad': cantidad, 'maximo':maximo, 'minimo':minimo, 'promedio':promedio}
        return cotizacion
