
# Receta Python 9-4: Leer un correo-e con IMAP.

import imaplib, getpass

servidor = imaplib.IMAP4('email.empresa.com')
servidor.login(getpass.getuser(), getpass.getpass())

servidor.select()
tipo, datos = servidor.search(None, 'ALL')

servidor.close()
servidor.logout()
