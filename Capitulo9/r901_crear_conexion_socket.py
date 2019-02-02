
# Receta Python 9-1: Crear una conexión de socket.

import socket

host = '192.168.0.13'
puerto = '5151'

s = socket.create_connection((host, puerto))


