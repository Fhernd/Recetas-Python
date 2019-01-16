# Reemplzar texto en una cadena caracteres:

frase = 'python.com es el sitio oficial de Python'

# Forma manual: uso de la notación slicing (o rebada)

frase_corregida = frase[0:7] + 'org' + frase[10:]

print(frase_corregida)

# Forma automática: uso del método replace:

frase_corregida = frase.replace('com', 'org')

print(frase_corregida)