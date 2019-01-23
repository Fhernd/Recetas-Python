
# Receta 3-4: Iterar el contenido de un archivo

archivo = open('archivo.csv')

for pais in archivo:
    print(pais)

archivo = open('archivo.csv')

print(next(archivo))
print(next(archivo))
print(next(archivo))
print(next(archivo))
