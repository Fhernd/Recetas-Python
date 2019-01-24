
# Receta 4-3: Leer el contenido de un archivo

# 1. Leer todo el contenido
# 2. Leer una parte
# 3. Utilizar un ciclo

archivo = open('paises.csv')

# 1. Lee todo el contenido del archivo:
# print(archivo.read())

# 2. Lee una parte (cantidad en bytes):
# lectura_parcial = archivo.read(10)
#
# print(lectura_parcial)

# 3. Uso de un ciclo:
for linea in archivo:
    print(linea, end='')
