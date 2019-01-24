
# Receta 4-4: Leer el contenido de un archivo XML:

import xml.etree.ElementTree as ET

archivo_xml = ET.parse('productos.xml')

raiz = archivo_xml.getroot()

print(raiz)

for hijo in raiz:
    print(hijo.text)
