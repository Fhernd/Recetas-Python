
# Receta 4-9: Crear un archivo ZIP.

from zipfile import ZipFile

nuevo_archivo = ZipFile('archivo.zip', 'a')

nuevo_archivo.write('paises.csv')
nuevo_archivo.write('productos.xml')

nuevo_archivo.close()
