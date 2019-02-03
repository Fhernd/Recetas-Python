
# Receta Python 9-8: Crear un servidor.

import socket

host = ''
puerto = '5353'

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((host, puerto))
servidor.listen(1)
