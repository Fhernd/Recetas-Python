
# Remover el espacio (o cualquier otro caracter) de una cadena caracteres:

lenguaje = "   Python es génial  "

print(lenguaje)
print(lenguaje.strip())

frase = 'xxxyyyxxx'

print(frase.strip('x'))

# rstrip(), lstrip()

print(frase.lstrip('x').rstrip('x'))

