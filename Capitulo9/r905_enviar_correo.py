
# Receta 9-5: Enviar correo-e.

import smtplib, getpass

servidor = smtplib.SMTP('email.empresa.co')
servidor.login(getpass.getuser(), getpass.getpass())

remitente = 'usuario1@gmail.com'
destinatario = 'usuario2@gmail.com'

mensaje = 'Python es un lenguaje de programación... génial'

servidor.sendmail(remitente, destinatario, mensaje)
