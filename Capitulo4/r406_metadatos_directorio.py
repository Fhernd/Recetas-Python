
# Receta 4-6: Obtener metadatos de un directorio

import os

directorio_actual = os.getcwd()

metadatos = os.stat(directorio_actual)

print(metadatos)
print(metadatos.st_ctime)
