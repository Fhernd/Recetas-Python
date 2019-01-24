
# Receta 4-5: Crear carpeta

import os

nuevo_directorio = 'nuevo_directorio'

if not os.path.exists(nuevo_directorio):
    os.makedirs(nuevo_directorio)
