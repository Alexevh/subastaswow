from . import datos as d



def buscarObjeto(diccionario, objeto):
    aciertos = 0
    errores = 0
    minimo = 0
    maximo = 0
    masbarato = ''
    mascaro = ''
    itemNro = 0
    cantidadtotal = 0
    montototal = 0
    itemNro = objeto

    for n in diccionario.values():
        for i in n:
            #print(i)
            try:
                if i['item'] == itemNro:
                    aciertos += 1
                    # Calculo el valor en oro de la unidad
                    valor = (i['buyout'] / i['quantity']) / 10000
                    cantidadtotal +=1
                    montototal += valor
                    if valor > maximo:
                        maximo = valor
                        mascaro = i['owner']
                    if valor < minimo or minimo == 0:
                        minimo = valor
                        masbarato = i['owner']
            except:
                errores += 1

    try:
        promedio = montototal / cantidadtotal
    except:
        promedio = 0

    resultado = {'minimo':minimo, 'maximo':maximo, 'mbarato': masbarato, 'mascaro':mascaro, 'promedio':promedio, 'cantidad':cantidadtotal}
    return resultado