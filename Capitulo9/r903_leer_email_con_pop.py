
# Receta Python 9-3: Leer un correo-e con POP.

import getpass, poplib

servidor = poplib.POP3('192.168.0.13')
servidor.user(getpass.getuser())
servidor.pass_(getpass.getpass)

cantidad_mensajes, bandeja = servidor.stat()

# En conjunto:
lista_correo = servidor.list()

# Un mensaje en particular:
mensaje = servidor.retr(2)
