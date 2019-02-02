
# Receta Python 9-2: Enviar datos sobre una conexión socket.

import socket

host = '192.168.0.13'
puerto = '5151'

s = socket.create_connection((host, puerto))

mensaje = b'Python es un lenguaje de programación tremendo'
longitud = len(mensaje)
total_enviado = 0

while total_enviado < longitud:
    enviado = s.send(mensaje[total_enviado:])
    total_enviado += enviado
