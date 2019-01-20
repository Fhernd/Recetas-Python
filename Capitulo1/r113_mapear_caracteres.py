
# Receta 1-13: Mapear caracteres de un objeto string

lenguaje = 'Pithon'

mapa = lenguaje.maketrans('ií', 'yy')
print(lenguaje)
print(lenguaje.translate(mapa))

lenguaje = 'Pyt    hon'
print(lenguaje)
lenguaje = lenguaje.translate(str.maketrans({' ': None}))
print(lenguaje)
