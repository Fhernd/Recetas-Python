
# Receta Python 9-7: Enviar una solicitud vía GET.

import urllib.request

solicitud = urllib.request.Request('https://jsonplaceholder.typicode.com/todos/1', method='GET')

respuesta = urllib.request.urlopen(solicitud)

print(respuesta.status)
print(respuesta.reason)
print(respuesta.read())
