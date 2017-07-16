import os
import zipfile

class zipFactory():

    def comprimirDirectorio(self, origen, destino, nombrearchivozip):

        ficheros = os.listdir(origen)
        ficherozip = zipfile.ZipFile(destino+'/'+nombrearchivozip, 'w')
        ficherozip.close()

        ficherozip = zipfile.ZipFile(destino + '/'+nombrearchivozip, 'a')

        for archivo in ficheros:
            ficherozip.write(origen+'/'+archivo)
        ficherozip.close()

        print(str(destino+'/'+nombrearchivozip))
